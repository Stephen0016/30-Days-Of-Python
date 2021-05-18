from datetime import *


def q1():
    current_day = datetime.now().day
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_hour = datetime.now().hour
    current_minute = datetime.now().minute
    current_timestamp = datetime.timestamp(datetime.now())

    print(current_day,current_month,current_year,current_hour,current_minute,current_timestamp)


def q2():
    now = datetime.now()
    print(now.strftime("%m/%d/%Y, %H:%M:%S"))


def q3():
    today = "5 December, 2019"
    date_object = datetime.strptime(today, "%d %B, %Y")        # %B not %m
    print(date_object)


def q4():
    today = date(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
    new_year = date(year=datetime.now().year+1, month=1, day=1)
    diff = new_year - today
    print('Time left for new year:', diff)


def q5():
    today = date(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
    before = date(year=1970, month=1, day=1)
    diff = today - before
    print(diff)


def q6():
    pass
    #Think, what can you use the datetime module for? Examples:
        # Time series analysis
        # To get a timestamp of any activities in an application
        # Adding posts on a blog