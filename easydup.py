'''
easydup.py
'''
import sys
import json
import click

from utils import prints
from utils import paths
from utils import commands
from classes.configs import Configs



@click.command()
@click.argument('is-init', type=bool)
@click.argument('is-new', type=bool)
@click.argument('is-modify', type=bool)
@click.argument('is-delete', type=bool)
@click.argument('is-all-configs', type=bool)
@click.argument('configs-key', type=str)
@click.argument('no-full', type=bool)
@click.argument('is-list', type=bool)
@click.argument('folder-path', type=str)
def _main(is_init, is_new, is_modify, is_delete, is_all_configs, configs_key, no_full, is_list, folder_path):
    '''
    Core command. Use easydup instead
    '''
    configs_path = paths.resolve_path(folder_path, 'easydup-configs.json')
    print(f"`configs_path` is `{configs_path}`")

    if is_init:
        with open(configs_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps({
                'default': Configs.prompt_create(configs_path).to_dict()
            }, indent=2))
        sys.exit(0)

    if not paths.is_entry(configs_path):
        prints.red(f"`{configs_path}` not found")
        sys.exit(1)
    if paths.is_folder(configs_path):
        prints.red(f"`{configs_path}` is not a file")
        sys.exit(1)
    with open(configs_path, 'r', encoding='utf-8') as file:
        configs_dict_dict = json.loads(file.read())

    if is_new:
        if configs_key == 'default':
            prints.red(f"Can't create `{configs_key}` configuration")
            sys.exit(1)
        configs_dict_dict[configs_key] = Configs.prompt_create(configs_path).to_dict()
        with open(configs_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(configs_dict_dict, indent=2))
        sys.exit(0)

    if configs_key not in configs_dict_dict:
        prints.red(f"`{configs_key}` configuration not found")
        sys.exit(1)
    configs = Configs.from_dict(configs_path, configs_dict_dict[configs_key])

    if is_modify:
        configs.prompt_modify()
        configs_dict_dict[configs_key] = configs.to_dict()
        with open(configs_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(configs_dict_dict, indent=2))
        sys.exit(0)

    if is_delete:
        if configs_key == 'default':
            prints.red(f"Can't delete `{configs_key}` configuration")
            sys.exit(1)
        del configs_dict_dict[configs_key]
        with open(configs_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(configs_dict_dict, indent=2))
        sys.exit(0)

    if is_list:
        commands.run(f"duplicity list-current-files \"{configs.key_destination_url}\"", True)
        commands.run(f"duplicity list-current-files \"{configs.data_destination_url}\"", True)
        sys.exit(0)

    configs_list = [
        configs
    ]
    if is_all_configs:
        configs_list = sorted([Configs.from_dict(configs_path, configs_dict) for configs_dict in configs_dict_dict.values()], lambda configs: configs.order)

    is_full = not no_full

    for configs in configs_list:

        commands.run(f"duplicity backup --verbosity info --progress{(' --full-if-older-than 1W' if is_full else '')} \"{paths.resolve_path('$HOME/.gnupg/')}\" \"{configs.key_destination_url}\"", True)
        commands.run(f"duplicity remove-all-but-n-full 1 --force \"{configs.key_destination_url}\"", True)
        commands.run(f"duplicity backup --verbosity info --progress{(' --full-if-older-than 1W' if is_full else '')} --encrypt-key \"{configs.key}\" --include-filelist \"{configs.filelist_path}\" \"{configs.source_path}\" \"{configs.data_destination_url}\"", True)
        commands.run(f"duplicity remove-all-but-n-full 1 --force \"{configs.data_destination_url}\"", True)



if __name__ == '__main__':
    # pylint: disable-next=no-value-for-parameter
    _main()
