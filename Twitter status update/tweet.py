import tweepy

# consumer data
consumer_key = 	'E*************s'
consumer_secret = 'Z*******************fX'
access_token = '8*************************R'
access_token_secret = '5****************************i'

# setting up Oauth and integrate with api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# tweet to post over account
tweet = input('Your tweet: ')
api.update_status(status=tweet)
