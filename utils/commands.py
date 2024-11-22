'''
This module is from samueva97.
Do not modify it
'''
import os
import subprocess

from utils import chars
from utils import prints



def run(command_str, is_print):
    '''
    Runs the command
    '''
    prints.blue(f" => {command_str}")
    if is_print:
        os.system(command_str)
        return
    subprocess_run = subprocess.run(command_str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    stdout = subprocess_run.stdout.decode()[:-1]
    stderr = subprocess_run.stderr.decode()[:-1]
    return f"{stdout or ''}{chars.NEW_LINE if stdout and stderr else ''}{stderr or ''}"



def nohup(command_str, environment_dict):
    '''
    Runs a command in detached mode
    '''
    run(f"{' '.join([f'{key}={value}' for key, value in environment_dict.items()] + [''])}nohup {command_str} >/dev/null 2>/dev/null &", True)
