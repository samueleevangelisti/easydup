'''
easydupconfigs.py
'''
import click

from utils import typechecks



class EasydupConfigs:
    '''
    pass
    '''



    def __init__(self, source_path, destination_url, filelist_path):
        typechecks.check(source_path, str)
        typechecks.check(destination_url, str)
        typechecks.check(filelist_path, str)
        self.source_path = source_path
        self.destination_url = destination_url
        self.filelist_path = filelist_path



    @staticmethod
    def prompt_create():
        '''
        pass
        '''
        return EasydupConfigs(click.prompt('source_path', type=str, default='.', show_default=True), click.prompt('destination_url', type=str), click.prompt('filelist_path', type=str, default='easydup-filelist.txt', show_default=True))
    


    @staticmethod
    def from_dict(configs_dict):
        '''
        pass
        '''
        return EasydupConfigs(configs_dict['source_path'], configs_dict['destination_url'], configs_dict['filelist_path'])
    


    def to_dict(self):
        return {
            'source_path': self.source_path,
            'destination_url': self.destination_url,
            'filelist_path': self.filelist_path
        }
