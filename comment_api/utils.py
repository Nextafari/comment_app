from random import randrange
from datetime import timedelta
from datetime import datetime
import os


# Gets the value of DEBUG from the OS env
def debug_status():
    if os.environ['DEBUG'] == 'False':
        return False
    else:
        return True


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def convert_to_random_days():
    years = [
        2001, 2002, 2003, 2004,
        2005, 2006, 2007, 2008,
        2009, 2010, 2011, 2013,
        2019
    ]
    d1 = None
    d2 = None
    arg = None
    for year in years:
        date = f'1/1/{year} 1:30 PM'
        val = randrange(20)
        y_delta = year + val
        date_2 = f'1/1/{y_delta} 4:50 AM'

        d1 = datetime.strptime(date, '%m/%d/%Y %I:%M %p')
        d2 = datetime.strptime(date_2, '%m/%d/%Y %I:%M %p')
        arg = datetime.now() - d1
        arg = str(arg).split(" ")

    print(d1, d2)
    print(random_date(d1, d2))

    return randrange(int(arg[0]))
