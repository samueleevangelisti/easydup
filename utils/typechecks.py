'''
This module is from samueva97.
Do not modify it
'''
def check(variable, *type_list):
    '''
    Raises an exception if vrong type

    Parameters
    ----------
    variable : any
        Variable to check
    *type_list : list<types | None>
        Accepted types
    '''
    if variable is None and None in type_list:
        return
    variable_type = type(variable)
    if variable_type not in type_list:
        raise TypeError(f"Type `{variable_type}` not allowed")
