import tweepy
from collections import deque

# key and token for oauth process
consumer_key = 	'h********************f'
consumer_secret = 'g****************************mt'
access_token = '8****************************R'
access_token_secret = '5*******************************Ci'

# setting up Oauth and integrate with api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

limit = 100
account = ['youtube', 'twitter']

# getting set of accounts that my id is following
acc = api.me()
print('signed in with: ', acc.screen_name)
following = set(api.friends_ids())
print('total following ', len(following))

# list of no. of followers of given 2 accounts
q = deque()
for i in account:
    users = api.get_user(i)
    q.append(users.id)
print(q)

# get follow list
while len(q) > 0 and limit > 0:
    account_following = api.followers_ids(q[1])
    print('account id: ', q[1], 'followers counts ', len(account_following))
    for i in account_following:
        if i not in following:
            q.append(i) # q is new deque list
    if q[1] not in following:    # q[1] i.e twitter will be followed if not present in list
        follow = api.create_friendship(q[1])
        following.add(q[1])
        print('followed ', q[1])
        #limit -= 1
    q.popleft()

    if len(q) > limit:
        break

# follow the user
while len(q) > 0 and limit > 0:
    follow = api.create_friendship(q[0])
    print('followed ', q[0]) # q[0] is 0th elements in q.append(i)
    q.popleft()
