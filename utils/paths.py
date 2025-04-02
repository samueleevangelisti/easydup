'''
This module is from samueva97.
Do not modify it
'''
from os import path



def resolve_variables(*entry_path_list):
    '''
    Resolved the variables in input path
    '''
    return path.expandvars(path.join(*entry_path_list))



def resolve_path(*entry_path_list):
    '''
    Resolves the input path and returns the absolute path
    '''
    return path.abspath(resolve_variables(*entry_path_list))



def resolve_link_path(*entry_path_list):
    '''
    Resolves the input path following symbolic links
    '''
    return path.realpath(resolve_path(*entry_path_list))



def is_absolute(*entry_path_list):
    '''
    Return true if path is absolute
    '''
    return path.isabs(resolve_variables(*entry_path_list))



def is_entry(*entry_path_list):
    '''
    Returns true if entry exists
    '''
    return path.exists(resolve_path(*entry_path_list))



def is_folder(*entry_path_list):
    '''
    Returns true if entry is folder
    '''
    return path.isdir(resolve_path(*entry_path_list))



def is_inside(entry_path, folder_path):
    '''
    Returns true if entry is inside folder
    '''
    absolute_folder_path = resolve_path(folder_path)
    return path.commonpath((
        resolve_path(entry_path),
        absolute_folder_path,
    )) == absolute_folder_path



def get_folder_path(*entry_path_list):
    '''
    Returns the folder path
    '''
    return path.dirname(resolve_path(*entry_path_list))



def get_file_name(*entry_path_list):
    '''
    Returns the folder path
    '''
    return path.basename(resolve_path(*entry_path_list))
