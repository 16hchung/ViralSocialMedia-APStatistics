import twitter
import json

# ======= AUTHORIZATION =======

CONSUMER_KEY = '25Oig8zX3WlimFynDQ3GjNFZS'
CONSUMER_SECRET = 'la2Gvg0upRO2bNg1oGsqA1kJiG2dxr2IO8HGmC3f5bK60qGJ0u'
OAUTH_TOKEN = '1661162772-nNYuZSQxaoHnT0lVCSdhcPcWoHuoAk3LiYJVIyd'
OAUTH_TOKEN_SECRET = 'XW1RMQptZOvQZVnpVP2O9ymlRElgQ98ThDpRYGzzoNzuE'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

# print twitter_api

# ==================================

q = '#bringbackourgirls'
count = 100

search_results = twitter_api.search.tweets(q=q, count=count)
statuses = search_results['statuses']
print len(statuses)
tweet = statuses[80]

print tweet['text']

# print json.dumps(statuses[0], indent=1)