"""
Parse KML file from google maps
"""

import re
float_pattern = re.compile("[+-]?\d*\.\d+")
def parse_kml(f):
  lines = []
  for l in open(f):
    if '<coordinates>' in l:
      lines.append(l.strip())

  coords = [parse_coordinate_line(l) for l in lines]
  return coords

def parse_coordinate_line(l):
  coords = re.findall(float_pattern, l)
  coords = [float(n) for n in coords]
  return coords