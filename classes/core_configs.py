'''
core_configs.py
'''
from datetime import datetime

from utils import typechecks



class CoreConfigs:
    '''
    easydup core configs
    '''



    def __init__(self, sync_datetime):
        '''
        Parameters
        ----------
        sync_datetime : datetime
            Last sync datetime
        '''
        typechecks.check(sync_datetime, datetime)
        self.sync_datetime = sync_datetime



    @staticmethod
    def from_dict(configs_dict):
        '''
        Create configs from dict

        Parameters
        ----------
        configs_dict : dict
            Configs in dict
        
        Returns
        -------
        CoreConfigs
        '''
        return CoreConfigs(datetime.fromisoformat(configs_dict['sync_datetime']))



    def to_dict(self):
        '''
        Return configs in dict

        Returns
        -------
        dict
        '''
        return {
            'sync_datetime': self.sync_datetime.isoformat()
        }
