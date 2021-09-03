from app.controllers.auth import *

def get_limit(limit):
  defaultLimit = 30
  if limit is None:
    limit = defaultLimit
  else:
    try:
      limit = int(limit)

      # limit must be between 5 and 100
      if limit < 10 or limit > 100:
        limit = defaultLimit
    except ValueError:
      limit = defaultLimit
  return limit

def get_and_parse_tweets(hashtag, limit):
  tweet_fields = "tweet.fields=author_id,created_at,entities,public_metrics,text"
  max_results = limit
  url = "https://api.twitter.com/2/tweets/search/recent?query=%23{}&{}&max_results={}".format(hashtag, tweet_fields, max_results)
  
  json_response = connect_to_endpoint(url)

  if json_response['meta']['result_count'] == 0:
    return {'error': 'no Tweets found with that hashtag'}, str, True
  

  tweets = []
  ids = ""
  for data in json_response['data']:
    tweet = {}
    
    tweet['date'] = data['created_at']

    if 'entities' in data and 'hashtags' in data['entities']:
      tweet['hashtags'] = []
      for hashtags in data['entities']['hashtags']:
        tweet['hashtags'].append(hashtags['tag'])

    tweet['metrics'] = data['public_metrics']

    tweet['text'] = data['text']
    
    tweet['author_id'] = data['author_id']
    ids += data['author_id'] + ','

    tweets.append(tweet)

  return tweets, ids[:-1], False


def get_account_info(ids):
  url = "https://api.twitter.com/2/users?ids={}".format(ids)
  json_response = connect_to_endpoint(url)
  
  return json_response['data']

  
def create_response_dict(info, tweets): 
  response_dict = []
  
  for i in range(len(info)):
    response_dict.append( {'account': info[i], 'tweet': tweets[i]} )
  
  return response_dict


def get_tweets_from_hashtags(hashtag, limit):  
  limit = get_limit(limit)

  tweets, ids, error = get_and_parse_tweets(hashtag, limit)
  if error:
    return tweets

  info = get_account_info(ids)

  response_dict = create_response_dict(info, tweets)

  return response_dict