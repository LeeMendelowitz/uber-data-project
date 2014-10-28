from keys import keys
from UberAPI import UberAPI
uber = UberAPI(keys.SERVER_TOKEN)
import UberUtils
res = UberUtils.get_times_as_geojson(uber, points)
print res