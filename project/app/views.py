
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from app.controllers.user_tweets import get_tweets_from_username
# import app.controllers.user_tweets as user_tweets


def getLimit(limit):
  defaultLimit = 30
  if limit is None:
    limit = defaultLimit
  else:
    try:
      limit = int(limit)

      # limit must be between 5 and 100
      if limit < 5 or limit > 100:
        limit = defaultLimit
    except ValueError:
      limit = defaultLimit
  return limit
    
class hashtagsList(APIView):
    def get(self, request, hashtag=None):

      limit = getLimit(request.GET.get('limit'))

      return Response({'hashtag': hashtag, 'limit': limit})

class userTweetsList(APIView):
    def get(self, request, user=None):
      
      limit = getLimit(request.GET.get('limit'))

      response_dict = get_tweets_from_username(user, limit)

      # print(response_dict)

      return Response(response_dict)
