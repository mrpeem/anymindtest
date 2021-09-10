import requests
import os
import json

bearer_token = "AAAAAAAAAAAAAAAAAAAAAFNRTQEAAAAAWv3PHQxSJTBTb3SOJFQWhGKBZQ8%3DD0nUOj6aXZ7mLBaSUKxDRVEvb5cOqoTjCjBR85jrWtlOmOpa55"

def bearer_oauth(r):
  """
  Method required by bearer token authentication.
  """

  r.headers["Authorization"] = f"Bearer {bearer_token}"
  r.headers["User-Agent"] = "v2TweetLookupPython"
  return r


def connect_to_endpoint(url, params):
  if params is None:
    response = requests.request("GET", url, auth=bearer_oauth)
  else:
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
  print(response.status_code)
  if response.status_code != 200:
      raise Exception(
          "Request returned an error: {} {}".format(
              response.status_code, response.text
          )
      )
  return response.json()