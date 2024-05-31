'''
easydupconfigs.py
'''
import click

from utils import typechecks
from utils import paths



class EasydupConfigs:
    '''
    easydup confings
    '''



    def __init__(self, file_path, order, original_source_path, original_key_destination_url, original_data_destination_url, key, original_filelist_path):
        typechecks.check(file_path, str)
        typechecks.check(order, int)
        typechecks.check(original_source_path, str)
        typechecks.check(original_key_destination_url, str)
        typechecks.check(original_data_destination_url, str)
        typechecks.check(original_filelist_path, str)
        self.folder_path = paths.folder_path(file_path)
        self.order = order
        self.original_source_path = original_source_path
        self.source_path = paths.resolve_path(self.folder_path, original_source_path)
        self.original_key_destination_url = original_key_destination_url
        self.key_destination_url = paths.resolve_variables(original_key_destination_url)
        self.original_data_destination_url = original_data_destination_url
        self.data_destination_url = paths.resolve_variables(original_data_destination_url)
        self.key = key
        self.original_filelist_path = original_filelist_path
        self.filelist_path = paths.resolve_path(self.folder_path, original_filelist_path)



    @staticmethod
    def prompt_create(file_path):
        '''
        Create the configs using a click prompt

        Parameters
        ----------
        file_path : str
            Path of the configs file

        Returns
        -------
        EasydupConfigs
        '''
        return EasydupConfigs(file_path, click.prompt('order', type=int, default=0, show_default=True), click.prompt('source_path', type=str, default='.', show_default=True), click.prompt('key_destination_url', type=str), click.prompt('data_destination_url', type=str), click.prompt('key', type=str), click.prompt('filelist_path', type=str, default='easydup-filelist.txt', show_default=True))



    def prompt_modify(self):
        '''
        Modify the configs using click prompts
        '''
        self.order = click.prompt('order', type=int, default=self.order, show_default=True)
        self.original_source_path = click.prompt('source_path', type=str, default=self.original_source_path, show_default=True)
        self.source_path = paths.resolve_path(self.folder_path, self.original_source_path)
        self.original_key_destination_url = click.prompt('key_destination_url', type=str, default=self.original_key_destination_url, show_default=True)
        self.key_destination_url = paths.resolve_variables(self.original_key_destination_url)
        self.original_data_destination_url = click.prompt('data_destination_url', type=str, default=self.original_data_destination_url, show_default=True)
        self.data_destination_url = paths.resolve_variables(self.original_data_destination_url)
        self.original_filelist_path = click.prompt('filelist_path', type=str, default=self.original_filelist_path, show_default=True)
        self.filelist_path = paths.resolve_path(self.folder_path, self.original_filelist_path)



    @staticmethod
    def from_dict(file_path, configs_dict):
        '''
        Create the configs from a dict

        Parameters
        ----------
        file_path : str
            Path of the configs file
        configs_dict : dict
            Dict containing the configs
        
        Returns
        -------
        EasydupConfigs
        '''
        return EasydupConfigs(file_path, configs_dict['order'], configs_dict['source_path'], configs_dict['key_destination_url'], configs_dict['data_destination_url'], configs_dict['key'], configs_dict['filelist_path'])



    def to_dict(self):
        '''
        Convert the configs to a dict

        Returns
        -------
        dict
        '''
        return {
            'order': self.order,
            'source_path': self.original_source_path,
            'key_destination_url': self.original_key_destination_url,
            'data_destination_url': self.original_data_destination_url,
            'key': self.key,
            'filelist_path': self.original_filelist_path
        }
