
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def getLimit(limit):
  defaultLimit = 30
  if limit == None:
    limit = defaultLimit
  else:
    try:
      limit = int(limit)
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

      return Response({'user': user, 'limit': limit})
