'''
This module is from samueva97.
Do not modify it
'''
from datetime import datetime
from datetime import timezone



def create(year, month, day, hour=0, minute=0, second=0, microsecond=0):
    '''
    Returns a datetime in utc
    
    Parameters
    ----------
    year : int
        Year
    month : int
        Month
    day : int
        Day
    hour : int
        Hour
    minute : int
        Minute
    second : int
        Second
    microsecond : int
        Microsecond
    
    Returns
    -------
    datetime
    '''
    return datetime(year, month, day, hour, minute, second, microsecond, tzinfo=timezone.utc)



def now():
    '''
    Returns actual datetime in utc

    Returns
    -------
    datetime
    '''
    return datetime.now(timezone.utc)



def today():
    '''
    Returns actual day datetime on 00:00:00

    Returns
    -------
    datetime
    '''
    return now().replace(hour=0, minute=0, second=0, microsecond=0)



def from_timestamp(timestamp):
    '''
    Returns datetime from a utc timestamp

    Returns
    -------
    datetime
    '''
    return datetime.fromtimestamp(timestamp, timezone.utc)



def from_iso(datetime_str):
    '''
    Returns datetime from string

    Parameters
    ----------
    datetime_str : str
        Datetime in iso string
    
    Returns
    -------
    datetime
    '''
    return_datetime = datetime.fromisoformat(datetime_str)
    return (return_datetime.replace(tzinfo=timezone.utc) if not return_datetime.tzinfo else return_datetime)
