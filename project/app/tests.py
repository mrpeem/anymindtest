from django.test import TestCase
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


from app.controllers.user_tweets import get_tweets_from_username
from app.controllers.hashtags_search import get_tweets_from_hashtags

# Create your tests here.
class Test(TestCase):
  def test_hashtags_no_limit(self):
    response_dict = get_tweets_from_hashtags('python', None)
    self.assertEquals(30, len(response_dict))

  def test_hashtags_invalid_limit(self):
    response_dict = get_tweets_from_hashtags('python', 'string')
    self.assertEquals(30, len(response_dict))

  def test_hashtags_out_of_bound_limit(self):
    response_dict = get_tweets_from_hashtags('python', 1)
    self.assertEquals(30, len(response_dict))

    response_dict = get_tweets_from_hashtags('python', 111)
    self.assertEquals(30, len(response_dict))

  def test_hashtags_valid_limit(self):
    response_dict = get_tweets_from_hashtags('python', 10)
    self.assertEquals(10, len(response_dict))

    response_dict = get_tweets_from_hashtags('python', 50)
    self.assertEquals(50, len(response_dict))
  
  def test_hashtags_contains_account_info(self):
    response_dict = get_tweets_from_hashtags('python', 10)
    self.assertTrue('account' in response_dict[0])
    self.assertTrue(response_dict[0]['account']['id'])
    self.assertTrue(response_dict[0]['account']['name'])
    self.assertTrue(response_dict[0]['account']['username'])

  def test_hashtags_contains_tweet_info(self):
    response_dict = get_tweets_from_hashtags('python', 10)
    self.assertTrue('tweet' in response_dict[0])
    self.assertTrue(response_dict[0]['tweet']['date'])
    self.assertTrue(response_dict[0]['tweet']['hashtags'])
    self.assertTrue(response_dict[0]['tweet']['metrics'])
    self.assertTrue(response_dict[0]['tweet']['text'])

  def test_hashtags_contains_hashtag(self):
    response_dict = get_tweets_from_hashtags('python', 10)
    self.assertTrue('tweet' in response_dict[0])
    for data in response_dict:
      hashtags = data['tweet']['hashtags']
      hashtags = [x.lower() for x in hashtags]
      print(hashtags)
      if 'python' not in hashtags:
        print(data['tweet']['text'])
      self.assertTrue('python' in hashtags)

    
