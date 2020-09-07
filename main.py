import config, tweepy, time, datetime, math
from datetime import datetime
from dateutil import relativedelta
from time import sleep 

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.token_secret)
api = tweepy.API(auth)

start_date = datetime(2018, 8, 18)
curr_date = datetime.today()

diff = relativedelta.relativedelta(curr_date, start_date)
t_years = diff.years
t_months = diff.months
t_days = diff.days

def build_string(years, months, days):
    msg = "Whole Lotta Red has NOT been released.\n"
    msg += "It's been " + str(years) + " years"
    if(months == 0):
        if(days != 0):
            msg += " and " + str(days) + " days"

    else:
        if(days != 0):
            msg += ", " + str(months) + " months"
            msg += " and " + str(days) + " days"
        else:
            msg += " and " + str(months) + " months"
    
    msg += " since the project has been announced."
    return msg

t_msg = build_string(t_years, t_months, t_days)
print(t_msg)

while True:
    curr_time = time.localtime()
    hour = curr_time.tm_hour
    min = curr_time.tm_min
    sec = curr_time.tm_sec

    # print (msg)
    
    if hour == 11 and min == 3 and sec == 0:   
        years = diff.years
        months = diff.months
        days = diff.days

        msg = build_string(years, months, days)
        print(msg)
        # api.update_status(msg)


