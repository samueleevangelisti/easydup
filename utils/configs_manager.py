'''
configs_manager.py
'''
import json
import click

from classes.configs_2025_04_15 import Configs20250415
from classes.configs_2025_04_16 import Configs20250416



_CURRENT_VERSION = '2025-04-16'
_CURRENT_CLASS = Configs20250416









class ConfigsException(Exception):
    pass









def migrate_configs_dict_dict(file_path, configs_dict_dict):
    is_migration = False
    for configs_key, configs_dict in configs_dict_dict.items():
        print(f"configs_key: {configs_key}")
        configs = None
        match configs_dict['version']:
            case '2025-04-16':
                configs = Configs20250416.from_dict(file_path, configs_dict)
            case '2025-04-15':
                configs = Configs20250415.from_dict(file_path, configs_dict)
            case _:
                raise ConfigsException('`version` not valid')
        is_configs_migration = False
        while configs.version != _CURRENT_VERSION:
            match configs.version:
                case '2025-04-15':
                    is_configs_migration = True
                    configs = Configs20250416(file_path, configs.order, configs.original_source_path, configs.original_key_destination_url, configs.original_data_destination_url, click.prompt('full_period', type=str, default='1M', show_default=True), configs.key, configs.original_filelist_path)
        if is_configs_migration:
            configs_dict_dict[configs_key] = configs.to_dict()
        is_migration = is_migration or is_configs_migration
    if is_migration:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(configs_dict_dict, indent=2))




def prompt_create(file_path):
    return _CURRENT_CLASS.prompt_create(file_path)



def from_dict(file_path, configs_dict):
    if configs_dict['version'] != _CURRENT_VERSION:
        raise ConfigsException('`version` is old')
    return _CURRENT_CLASS.from_dict(file_path, configs_dict)
