import geocoder
g = geocoder.ip('me')
print(g.latlng)

# from geopy.geocoders import Nominatim
#
# # calling the nominatim tool
# geoLoc = Nominatim(user_agent="GetLoc")
#
# # passing the coordinates
# locname = geoLoc.reverse(g.latlng)
#
# # printing the address/location name
# print(locname.address)