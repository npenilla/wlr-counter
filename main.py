import config, tweepy, time

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.token_secret)
api = tweepy.API(auth)

curr_time = time.localtime()
print(curr_time)
# curr_clock = time.strfrtime("%H:%M:%S", curr_time)

hour = curr_time.tm_hour
min = curr_time.tm_min


api.update_status("Fuck bitches get money")
