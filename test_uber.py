from keys import keys
from GEOJSON import parse_geojson
points = parse_geojson('dc.geojson')
from UberAPI import UberAPI
uber = UberAPI(keys.SERVER_TOKEN)
import UberUtils
res = UberUtils.get_times_as_geojson(uber, points)
print res
