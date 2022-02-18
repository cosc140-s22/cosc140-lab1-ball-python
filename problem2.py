#
# Name: Kyle Shaw
# Collaborator(s): None
#
startlat = input("Where is your starting latitude? (degrees)")
startlon = input("Where is your starting longitude? (degrees)")
endlat = input("Where is your ending latitude? (degrees)")
endlon = input("Where is your ending longitude? (degrees)")
import math
rslat = math.radians(float(startlat))
rslon = math.radians(float(startlon))
relat = math.radians(float(endlat))
relon = math.radians(float(endlon))
dlon = relon - rslon
dlat = relat - rslat
a = (math.sin(dlat/2))**2+math.cos(rslat) * math.cos(relat) * (math.sin(dlon/2))**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
d = 3956 * c
print(f"{d} miles away from your starting point")
