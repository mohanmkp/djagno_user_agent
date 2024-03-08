from django.shortcuts import render, HttpResponse
from django.contrib.gis.geoip2 import GeoIP2
from geopy.geocoders import Nominatim



def get_location(latitude, longitude):
    # Initialize Nominatim geocoder
    geolocator = Nominatim(user_agent="geo_locator")

    # Combine latitude and longitude into a single string
    location = f"{latitude}, {longitude}"

    try:
        # Get location information based on latitude and longitude
        address = geolocator.reverse(location)

        # Extract relevant information from the address
        location_info = {
            'address': address.address,
            'city': address.raw.get('address', {}).get('city'),
            'country': address.raw.get('address', {}).get('country'),
            # Add more fields as needed
        }
    except Exception as e:
        # Handle any errors that occur during geocoding
        print(f"Error: {e}")
        location_info = None

    return location_info




def get_user_location(request):
    print(request.META['HTTP_USER_AGENT'])
    remote_addr = request.META.get('HTTP_X_FORWARDED_FOR')
    if remote_addr:
        address = remote_addr.split(',')[-1].strip()
        print("if ", address)
    else:
        address = request.META.get('REMOTE_ADDR')
        print("else ", address)

    geoip2 = GeoIP2()
    print(geoip2.country(address))
    print(geoip2.city(address))
    print(geoip2.lat_lon(address))

    latitude = 37.7749
    longitude = -122.4194
    location_info = get_location(latitude, longitude)
    print(location_info)
    return HttpResponse("done")


