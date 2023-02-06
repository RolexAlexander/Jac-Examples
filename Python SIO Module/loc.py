from geopy.geocoders import Nominatim
from jaseci.actions.live_actions import jaseci_action  # step 1

@jaseci_action(act_group=["location"], allow_remote=True)

def get_details(latitude, longitude):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(f'{latitude}, {longitude}', exactly_one=True)
    location = location.raw
    print(location)
    return location

@jaseci_action(act_group=["location"], allow_remote=True)
def get_latitude_longitude(location):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(location)
    print(location)
    return (location.latitude, location.longitude)
