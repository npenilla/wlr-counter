import config, tweepy, time, datetime, math
from datetime import datetime
from dateutil import relativedelta
from time import sleep

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.token_secret)
api = tweepy.API(auth)

curr_date = datetime.today()
start_date = datetime(2018, 8, 18)

diff = relativedelta.relativedelta(curr_date, start_date)
def build_string(years, months, days):
    msg = "Whole Lotta Red has still NOT been released.\n\n"
    msg += "It's been " + str(years) + " years"

    if(months == 0):
        if(days != 0):
            msg += " and " + str(days) + " days"

    else:
        if(days != 0):
	    if(months == 1){
		msg += ", " + str(months) + " month"
	    }
	    else{
            	msg += ", " + str(months) + " months"
	    }
            msg += " and " + str(days) + " days"
        else:
	    if(months == 1){
		msg += " and " + str(months) + " month"
	    }
            else {
	        msg += " and " + str(months) + " months"
	    }

    msg += " since @playboicarti has announced the album."
    return msg
years = diff.years
months = diff.months
days = diff.days
msg = build_string(years, months, days)
api.update_status(msg)

