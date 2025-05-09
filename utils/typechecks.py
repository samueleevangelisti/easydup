'''
This module is from samueva97.
Do not modify it
'''
def check(variable, *type_list, min_length=None, max_length=None):
    '''
    Raises an exception if vrong type

    Parameters
    ----------
    variable : any
        Variable to check
    *type_list : list<types | None>
        Accepted types
    length : int
        Max length of the variable
    '''
    if variable in type_list:
        return
    variable_type = type(variable)
    if variable_type not in type_list:
        raise TypeError(f"`{variable_type}` not allowed")
    if min_length:
        if len(variable) < min_length:
            raise TypeError('`variable` too short')
    if max_length:
        if len(variable) > max_length:
            raise TypeError('`variable` too long')
