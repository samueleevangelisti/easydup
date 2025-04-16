'''
configs_manager.py
'''
import click

from classes.configs_2025_04_15 import Configs20250415
from classes.configs_2025_04_16 import Configs20250416









class ConfigsException(Exception):
    pass









def prompt_create(file_path):
    return Configs20250416.prompt_create(file_path)



def from_dict(file_path, configs_dict):
    configs = None
    match configs_dict['version']:
        case '2025-04-15':
            configs = Configs20250415.from_dict(file_path, configs_dict)
        case '2025-04-16':
            configs = Configs20250416.from_dict(file_path, configs_dict)
        case _:
            raise ConfigsException('`version` not valid')
    while configs.version != '2025-04-16':
        match configs.version:
            case '2025-04-15':
                configs = Configs20250416(configs.filelist_path, configs.order, configs.original_source_path, configs.original_key_destination_url, configs.original_data_destination_url, click.prompt('full_period', type=str, default='1M', show_default=True), configs.key, configs.original_filelist_path)
    return configs
