import config, tweepy, time, datetime, math, os, random, PIL
from datetime import datetime
from dateutil import relativedelta
from time import sleep
from PIL import Image

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.token_secret)
api = tweepy.API(auth)

#Compresses image in case it's too large for Tweepy
def compress_img(file_name):
    image = Image.open(file_name)
    image.save(file_name, quality = 20, optimize = True)
    return file_name

photo_directory = '/home/pi/wlr-counter/carti-bot-photos'
file_name = random.choice(os.listdir(photo_directory))
file_name = os.path.join(photo_directory, file_name)

if(os.path.getsize(file_name) >= 3072000):
    file_name = compress_img(file_name)

curr_date = datetime.today()
start_date = datetime(2018, 8, 18)
diff = relativedelta.relativedelta(curr_date, start_date)

#Builds tweet message based on date 
def build_string(years, months, days):
    msg = "Whole Lotta Red has still NOT been released.\n\n"
    msg += "It's been " + str(years) + " years"

    if(months == 0):
        if(days != 0):
            msg += " and " + str(days) + " days"
    else:
        if(days != 0):
            if(months == 1):
                msg += ", " + str(months) + " month"
            else:
                msg += ", " + str(months) + " months"
            msg += " and " + str(days) + " days"
        else:
            if(months == 1):
                msg += " and " + str(months) + " month"           
            else:
                msg += " and " + str(months) + " months"
    msg += " since @playboicarti has announced the album."
    return msg

years = diff.years
months = diff.months
days = diff.days
msg = build_string(years, months, days)   
api.update_with_media(file_name, msg)

