'''
easydup.py
'''
import os
import sys
import json
import click
import getpass

from utils import prints
from utils import paths
from utils import commands
from utils import configs_manager
from utils.configs_manager import ConfigsException



@click.command()
@click.argument('is-init', type=bool)
@click.argument('is-configs-migration', type=bool)
@click.argument('is-new', type=bool)
@click.argument('is-modify', type=bool)
@click.argument('is-delete', type=bool)
@click.argument('is-all-configs', type=bool)
@click.argument('configs-key', type=str)
@click.argument('no-full', type=bool)
@click.argument('is-list', type=bool)
@click.argument('folder-path', type=str)
def _main(is_init, is_configs_migration, is_new, is_modify, is_delete, is_all_configs, configs_key, no_full, is_list, folder_path):
    '''
    Core command. Use easydup instead
    '''
    configs_path = paths.resolve_path(folder_path, 'easydup-configs.json')
    print(f"`configs_path` is `{configs_path}`")

    if is_init:
        with open(configs_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps({
                'default': configs_manager.prompt_create(configs_path).to_dict()
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

    if is_configs_migration:
        try:
            configs_manager.migrate_configs_dict_dict(configs_path, configs_dict_dict)
        except ConfigsException as configs_exception:
            prints.red(str(configs_exception))
            sys.exit(1)
        sys.exit(0)

    if is_new:
        if configs_key == 'default':
            prints.red(f"Can't create `{configs_key}` configuration")
            sys.exit(1)
        configs_dict_dict[configs_key] = configs_manager.prompt_create(configs_path).to_dict()
        with open(configs_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(configs_dict_dict, indent=2))
        sys.exit(0)

    if configs_key not in configs_dict_dict:
        prints.red(f"`{configs_key}` configuration not found")
        sys.exit(1)

    try:
        configs = configs_manager.from_dict(configs_path, configs_dict_dict[configs_key])
    except ConfigsException as configs_exception:
        prints.red(str(configs_exception))
        sys.exit(1)

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
        try:
            configs_list = sorted([configs_manager.from_dict(configs_path, configs_dict) for configs_dict in configs_dict_dict.values()], lambda configs: configs.order)
        except ConfigsException as configs_exception:
            prints.red(str(configs_exception))
            sys.exit(1)

    is_full = not no_full

    for configs in configs_list:
        commands.run(f"duplicity backup --verbosity info --progress{(f" --full-if-older-than {configs.full_period}" if is_full else '')} \"{paths.resolve_path('$HOME/.gnupg/')}\" \"{configs.key_destination_url}\"", True)
        commands.run(f"duplicity remove-all-but-n-full 1 --force \"{configs.key_destination_url}\"", True)
        os.environ['PASSPHRASE'] = getpass.getpass('passphrase: ')
        commands.run(f"duplicity backup --verbosity info --progress{(f" --full-if-older-than {configs.full_period}" if is_full else '')} --encrypt-key \"{configs.key}\" --include-filelist \"{configs.filelist_path}\" \"{configs.source_path}\" \"{configs.data_destination_url}\"", True)
        commands.run(f"duplicity remove-all-but-n-full 1 --force \"{configs.data_destination_url}\"", True)



if __name__ == '__main__':
    # pylint: disable-next=no-value-for-parameter
    _main()
