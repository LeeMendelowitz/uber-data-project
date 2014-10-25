"""
Quick implementation of the UBER API
"""
import requests

BASE = 'https://api.uber.com'

class UberAPI(object):

  endpoints = {
    'products' : ('v1/products', ('longitude, latitude')),
    'time' : ('v1/estimates/time', ('start_latitude', 'start_longitude'))
  }

  def __init__(self, server_token):
      self.server_token = server_token

  def products(self, longitude, latitude):
    u = 'v1/products'
    params = {'longitude' : longitude,
              'latitude' : latitude}
    return self._request(u, params)

  def time(self, start_longitude, start_latitude):
    u = 'v1/estimates/time'
    params = {'start_longitude' : start_longitude,
              'start_latitude' :start_latitude
              }
    return self._request(u, params)

  def _request(self, url, params = {}):
    url = '%s/%s'%(BASE, url)
    params['server_token'] = self.server_token
    return requests.get(url, params = params)
