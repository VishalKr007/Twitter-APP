import tweepy

# consumer data
consumer_key = 	'E0j9Emk2OAIjOJWIGxNtouo4s'
consumer_secret = 'Z1j8ltnynmCAkjruTbDviouBtAN3YL6vZfcFQ7YNV0vsedN0fX'
access_token = '810148484829609984-v2LoYkoIOvHgHsiFcY9hGF4EbQWwBQR'
access_token_secret = '51c7KbrG6F6I3XiSLslAiA5Otn2OQeJGx0MQ6oPgugACi'

# setting up Oauth and integrate with api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# tweet to post over account
tweet = input('Your tweet: ')
api.update_status(status=tweet)
