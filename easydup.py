'''
easydup.py
'''
import sys
import json
import click

from utils import prints
from utils import paths
from utils import commands
from classes.easydupconfigs import EasydupConfigs



@click.command()
@click.argument('is-init', type=bool, default=False)
@click.argument('is-new', type=bool, default=False)
@click.argument('is-modify', type=bool, default=False)
@click.argument('is-delete', type=bool, default=False)
@click.argument('is-all-configs', type=bool, default=False)
@click.argument('configs-key', type=str, default='default')
@click.argument('is-list', type=bool, default=False)
@click.argument('folder-path', type=str, default='.')
def _main(is_init, is_new, is_modify, is_delete, is_all_configs, configs_key, is_list, folder_path):
    '''
    Core command. Use easydup instead
    '''
    configs_path = paths.resolve_path(folder_path, 'easydup-configs.json')
    print(f"`configs_path` is `{configs_path}`")

    if is_init:
        with open(configs_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps({
                'default': EasydupConfigs.prompt_create(configs_path).to_dict()
            }, indent=2))
        sys.exit(0)

    if not paths.is_entry(configs_path):
        prints.red(f"`{configs_path}` not found")
        sys.exit(1)
    if paths.is_folder(configs_path):
        prints.red(f"`{configs_path}` is not a file")
        sys.exit(1)
    with open(configs_path, 'r', encoding='utf-8') as file:
        easydup_configs_dict_dict = json.loads(file.read())

    if is_new:
        if configs_key == 'default':
            prints.red(f"Can't create `{configs_key}` configuration")
            sys.exit(1)
        easydup_configs_dict_dict[configs_key] = EasydupConfigs.prompt_create(configs_path).to_dict()
        with open(configs_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(easydup_configs_dict_dict, indent=2))
        sys.exit(0)

    if configs_key not in easydup_configs_dict_dict:
        prints.red(f"`{configs_key}` configuration not found")
        sys.exit(1)
    easydup_configs = EasydupConfigs.from_dict(configs_path, easydup_configs_dict_dict[configs_key])

    if is_modify:
        easydup_configs.prompt_modify()
        easydup_configs_dict_dict[configs_key] = easydup_configs.to_dict()
        with open(configs_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(easydup_configs_dict_dict, indent=2))
        sys.exit(0)

    if is_delete:
        if configs_key == 'default':
            prints.red(f"Can't delete `{configs_key}` configuration")
            sys.exit(1)
        del easydup_configs_dict_dict[configs_key]
        with open(configs_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(easydup_configs_dict_dict, indent=2))
        sys.exit(0)

    if is_list:
        commands.run(f"duplicity list-current-files \"{easydup_configs.key_destination_url}\"", True)
        commands.run(f"duplicity list-current-files \"{easydup_configs.data_destination_url}\"", True)
        sys.exit(0)

    easydup_configs_list = [
        easydup_configs
    ]
    if is_all_configs:
        easydup_configs_list = sorted([EasydupConfigs.from_dict(configs_path, easydup_configs_dict) for easydup_configs_dict in easydup_configs_dict_dict.values()], lambda easydup_configs: easydup_configs.order)

    for easydup_configs in easydup_configs_list:

        commands.run(f"duplicity backup --verbosity info --progress --full-if-older-than 1W \"{paths.resolve_path('$HOME/.gnupg/')}\" \"{easydup_configs.key_destination_url}\"", True)
        commands.run(f"duplicity remove-all-but-n-full 1 --force \"{easydup_configs.key_destination_url}\"", True)
        commands.run(f"duplicity backup --verbosity info --progress --full-if-older-than 1W --encrypt-key \"{easydup_configs.key}\" --include-filelist \"{easydup_configs.filelist_path}\" \"{easydup_configs.source_path}\" \"{easydup_configs.data_destination_url}\"", True)
        commands.run(f"duplicity remove-all-but-n-full 1 --force \"{easydup_configs.data_destination_url}\"", True)



if __name__ == '__main__':
    # pylint: disable-next=no-value-for-parameter
    _main()
