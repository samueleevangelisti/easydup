'''
easydupcoreconfigs.py
'''
from datetime import datetime
import json

from utils import typechecks



class EasydupCoreConfigs:
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
        EasydupCoreCOnfigs
        '''
        return EasydupCoreConfigs(datetime.fromisoformat(configs_dict['sync_datetime']))



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
