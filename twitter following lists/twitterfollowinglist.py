import twitter


# key and token to authentication
'''notes: change key and token details'''

consumer_key = 	'E0j9Emk2OAIjOJWIGxNtouo4s'
consumer_secret = 'Z1j8ltnynmCAkjruTbDviouBtAN3YL6vZfcFQ7YNV0vsedN0fX'
access_token = '810148484829609984-v2LoYkoIOvHgHsiFcY9hGF4EbQWwBQR'
access_token_secret = '51c7KbrG6F6I3XiSLslAiA5Otn2OQeJGx0MQ6oPgugACi'

# api authentication process
api = twitter.Api(consumer_key, consumer_secret, access_token, access_token_secret)

users = api.GetFriends()

# returns all the account that you are following
following = list()
for user in users:
    a = user.screen_name
    following.append(a)
    following.sort()
print(following)
