from django.shortcuts import render, HttpResponse
from django.contrib.gis.geoip2 import GeoIP2




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
    country = geoip2.country(request.META['REMOTE_ADDR'])
    print(country)

    return HttpResponse("done")


