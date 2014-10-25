"""
Quick implementation of the UBER API
"""
import requests
from geojson import Point, Feature

def time_json_to_str(response):
  """
  Format the json response from time endpoint into a summary string.
  """
  j = response.json()
  times = j['times']
  res = []
  for d in times:
    res.append('%s: %.1f'%(d['display_name'], d['estimate']))
  return '\n'.join(res)

def get_times_as_geojson(uber, coords):
  """
  Use UberAPI to get times for each point in coords.
  
  coords: iterable of lon,lat
  """

  features = []
  for lon,lat in coords:
    print lon,lat
    res = uber.time(lon, lat)
    point = Point(coordinates = (lon,lat))
    feature = Feature(geometry = point, properties = {'uber' : time_json_to_str(res)})
    features.append(feature)
  return features



