import twitter


# key and token to authentication
'''notes: change key and token details'''

consumer_key = 	'E**************s'
consumer_secret = 'Z************fX'
access_token = '8********************R'
access_token_secret = '5*******************i'

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
