from datetime import date, datetime

current_year = datetime.now().year


def is_leap_year(year):
    """
    A function to determine if a year is a leap year.
    """
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)


def gen_secs():
    """
    yield seconds from 0 - 59
    """
    sec = -1
    while sec < 59:
        sec += 1
        yield sec


def gen_minutes():
    """
    yield minutes from 0 - 59
    """
    minute = -1
    while minute < 59:
        minute += 1
        yield minute


def gen_hours():
    """
    yiel hours from 0 - 23
    """
    hour = -1
    while hour < 23:
        hour += 1
        yield hour


def gen_years(start=current_year):
    """
    yield years from start to the current year
    """
    start -= 1
    while start < datetime.now().year:
        start += 1
        yield start


def gen_month():
    """
    yield month from 1 to 12
    """
    month = 0
    while month < 12:
        month += 1
        yield month


def gen_days(month, leap_year=True):
    """
    return a generator which represent the
    amount of days in month argrument
    """
    days = 0
    if month in [4, 6, 9, 11]:
        days = 30

    elif month == [1, 3, 5, 7, 8, 10, 12]:
        days = 31

    elif month == 2 and leap_year:
        days = 29

    elif month == 2 and not leap_year:
        days = 28

    return (day for day in range(1, days + 1))


def gen_time():
    """
    yield all daily (hour:minute:second) options
    """
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                dt = datetime(2020, 12, 27, hour, minute, sec)
                yield dt.strftime("%H:%M:%S")


def gen_date():
    for year in gen_years():
        for month in gen_month():
            for day in gen_days(month, is_leap_year(year)):
                dt = datetime(year, month, day)
                yield dt.strftime("%m/%d/%Y")


def gen_date_time():
    for date in gen_date():
        for time in gen_time():
            yield f'{date} {time}'


def main():
    g = gen_date()
    for _ in range(0, 5):
        print(next(g))


if __name__ == "__main__":
    main()
