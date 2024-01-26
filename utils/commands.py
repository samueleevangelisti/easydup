'''
commands.py
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
        return None
    subprocess_run = subprocess.run(command_str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    stdout = subprocess_run.stdout.decode()[:-1]
    stderr = subprocess_run.stderr.decode()[:-1]
    return f"{stdout or ''}{chars.NEW_LINE if stdout and stderr else ''}{stderr or ''}"



def nohup(command_str):
    '''
    Runs a command in detached mode
    '''
    command_list = command_str.split(' ')
    index = 0
    while '=' in command_list[index]:
        index += 1
    run(f"{' '.join(command_list[:index] + [''])}nohup{' '.join([''] + command_list[index:] + [''])}>/dev/null 2>/dev/null &", True)



def google(url):
    '''
    Open a google chrome tab
    '''
    nohup(f"google-chrome-stable --start-maximized {url}")
