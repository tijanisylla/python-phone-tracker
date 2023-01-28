import phonenumbers
from myphone import api_key
from phonenumbers import geocoder, carrier, timezone
from opencage.geocoder import OpenCageGeocode
import folium

print("Enter your phone number :")
number =  input()
pepnumber = phonenumbers.parse(number, None)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

# Number +22237892196
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

if number:
    geocoder = OpenCageGeocode(api_key)
    query = str(location)
    result = geocoder.geocode(query)

    lat  = result[0]['geometry']['lat']
    lng  = result[0]['geometry']['lng']
    print(lat,lng)
    my_map = folium.Map(location=[lat,lng], zoom_start=9)
    folium.Marker([lat,lng], popup=location).add_to(my_map)
    my_map.save("myLocation.html")
    print("Map saved successfully")
else:
    print("Enter a valid phone number")


# Today we're going to be writgin a program with Python that will take a phone number and return the location of the phone number.
# This video is only for educational purposes and I recommend tracking your own phone number not others.
# We're going to be using 3 libararies
# We're going to be using the phonenumbers,opencage and folium library to do this.
# We're going to be using the opencage library to get the latitude and longitude of the phone number.



