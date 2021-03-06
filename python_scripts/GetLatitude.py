import requests
from GetDistance import Point
from geopy.geocoders import Nominatim

#{'place_id': '9167009604', 'type': 'attraction', ..

key = "AIzaSyAOWEPWyJI_9NZ0H_5rDaDp7jt2eVn-KC0"
str1 = "https://maps.googleapis.com/maps/api/geocode/json?address="
str2 = "&key="

def format(s):
    build = ""
    for i in range(len(s)):
        succ = s[i]
        if succ == ' ':
            build += '+'
        else:
            build += succ
    return build

def get_latitude(s):
    url = str1 + format(s) + str2 + key
    r = requests.get(url)
    data = r.json()
    loc = data.get("results")[0].get("geometry").get("location")
    return Point(loc.get("lat"), loc.get("lng"))

'''
def get_latitude(address):
    geolocator = Nominatim(user_agent="ParanoidPassenger")
    location = geolocator.geocode(address)
    print(location.latitude, location.longitude)
    return Point(location.latitude, location.longitude)
'''