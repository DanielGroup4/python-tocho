from unittest import result
import phonenumbers
import opencage
import folium
from my_phone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "es")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "es"))

from opencage.geocoder import OpenCageGeocode

key = "be2634affee049cd8c6a44ee40ce5711"
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]["geometry"]["lat"]
lng = results[0]["geometry"]["lng"]
print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save("find_location.html")
