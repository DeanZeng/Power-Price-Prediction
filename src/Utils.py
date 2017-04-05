from datetime import datetime

def ARSO_datetime_to_epoch(datetime_string):
    """Convert ARSO datetime into epoch time in seconds"""
    utc_time = datetime.strptime(datetime_string, "%Y-%m-%d %H:%M")
    epoch_time = (utc_time - datetime(1970, 1, 1)).total_seconds()
    return epoch_time

def ARSO_datetime_to_epoch_array(datetime_strings):
    """Convert list of ARSO datetimes into epoch time in seconds"""
    return [ARSO_datetime_to_epoch(dt) for dt in datetime_strings]