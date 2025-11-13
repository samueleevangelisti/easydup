'''
This module is from samueva97.
Do not modify it
'''
NONE = '\033[0m'
GREY = '\033[90m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
ORANGE = '\033[33m'
RED = '\033[91m'



def _color(text, color):
    return f"{color}{str(text).replace('\n', f"{NONE}\n{color}")}{NONE}"



def grey(text):
    '''
    Returns the text colored in grey

    Parameters
    ----------
    text : any
        The text

    Returns
    -------
    str
    '''
    return _color(text, GREY)



def blue(text):
    '''
    Returns the text colored in blue

    Parameters
    ----------
    text : any
        The text

    Returns
    -------
    str
    '''
    return _color(text, BLUE)



def purple(text):
    '''
    Returns the text colored in purple

    Parameters
    ----------
    text : any
        The text

    Returns
    -------
    str
    '''
    return _color(text, PURPLE)



def green(text):
    '''
    Returns the text colored in green

    Parameters
    ----------
    text : any
        The text

    Returns
    -------
    str
    '''
    return _color(text, GREEN)



def yellow(text):
    '''
    Returns the text colored in yellow

    Parameters
    ----------
    text : any
        The text

    Returns
    -------
    str
    '''
    return _color(text, YELLOW)



def orange(text):
    '''
    Returns the text colored in orange

    Parameters
    ----------
    text : any
        The text

    Returns
    -------
    str
    '''
    return _color(text, ORANGE)



def red(text):
    '''
    Returns the text colored in red

    Parameters
    ----------
    text : any
        The text

    Returns
    -------
    str
    '''
    return _color(text, RED)
