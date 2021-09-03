from app.controllers.auth import *

def get_info_from_username(username):
  """ Function that gets information regarding the user from username

  Args:
    param1 (str): username to look up
  Returns:
    dict: 
      - dict containing userid, name, and username (if no error)
      - error message if encoutnered error
    bool: whether the API returned an error; True if error, False if no error 
  """

  url = "https://api.twitter.com/2/users/by/username/{}".format(username)
  json_response = connect_to_endpoint(url)

  if 'errors' in json_response:
    return {'error': json_response['errors'][0]['detail']}, True
  else:
    return json_response['data'], False


def get_tweets_from_id(id, limit):
  tweet_fields = "tweet.fields=author_id,created_at,entities,public_metrics,text"
  max_results = limit
  url = "https://api.twitter.com/2/users/{}/tweets?{}&max_results={}".format(id, tweet_fields, max_results)
  json_response = connect_to_endpoint(url)
  return json_response['data']


def create_response_dict(info, tweets):
  response_dict = {'account': info, 'tweets': []}
  
  # iterate through all tweets
  for data in tweets:
    # create empty dict to contain info about tweet
    tweet = {}
    
    # add date data to tweet dict
    tweet['date'] = data['created_at']
    
    # add all hashtags in tweet to dict
    if 'entities' in data and 'hashtags' in data['entities']:
      tweet['hashtags'] = []
      
      for hashtags in data['entities']['hashtags']:
        tweet['hashtags'].append(hashtags['tag'])
    
    # add metrics such as likes, replies, retweets to tweet dict
    tweet['metrics'] = data['public_metrics']
    
    # add text to tweet dict
    tweet['text'] = data['text']
    
    response_dict['tweets'].append(tweet)

  return response_dict


def get_tweets(user, limit):  
  info, error = get_info_from_username(user)
  if error:
    return info

  tweets = get_tweets_from_id(info['id'], limit)

  response_dict = create_response_dict(info, tweets)

  return response_dict


