import sys, re, json

from time import mktime
from datetime import datetime
from main import show_logs

# truncate the file name and collect all args passed in cli
args = sys.argv[1:]

def date_to_timestamp(datetime_str):
    return mktime(datetime.strptime(datetime_str, "%d/%m/%Y %H:%M").timetuple())

def time_validator(time):
    # check if time matches format
    is_time_format = bool(re.match('[0-9]{1,2}:[0-9]{2}$', time))

    if not is_time_format:
        print("Invalid Time: The format for Time is not right!")

    return is_time_format

def date_validator(date):
    # check if date matches format
    is_date_format = bool(re.match('([0-9]{1,2}/{1}){2}[0-9]{4}$', date))

    if not is_date_format:
        print("Invalid Date: The format for date is not right!")
    
    return is_date_format


def search(start_date, start_time, end_date, end_time):
    if end_time is None:
        end_time = '23:59'
    
    if start_date is None:
        start_date = '01/01/2000'
    
    if start_time is None:
        start_time = '00:00'

    if not date_validator(start_date):
        return

    if not time_validator(start_time):
        return
    
    if not date_validator(end_date):
        return

    if not time_validator(end_time):
        return
    
    start_datetime_str = f'{start_date} {start_time}'
    end_datetime_str = f'{end_date} {end_time}'

    start_timestamp = date_to_timestamp(start_datetime_str)
    end_timestamp = date_to_timestamp(end_datetime_str)

    condition = lambda time: start_timestamp <= date_to_timestamp(time) <= end_timestamp
    show_logs(DATA, condition)


def main():
    # initialize variables
    start_date = start_time = end_date = end_time = None

    # re-assign to args passed
    if len(args) == 1:
        end_date = args[0]
    
    elif len(args) == 4:
        start_date, start_time, end_date, end_time = args

    else:
        print('No Arguments supplied')
    
    print(start_date, start_time, end_date, end_time)
    search(start_date, start_time, end_date, end_time)

if __name__ == "__main__":
    with open('cash_register_backup.json') as f:
        DATA = json.load(f)

    main()
