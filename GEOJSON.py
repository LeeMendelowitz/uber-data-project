"""
Parse geojson file
"""

import geojson
def parse_geojson(f):
  with open(f) as l:
    obj = geojson.load(l)
    coords = parse_coordinates(obj)
  return(coords)

def parse_coordinates(o):
  coords = geojson.utils.coords(o.features)
  coords = list(coords)
  return coords
