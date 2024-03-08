from django.shortcuts import render, HttpResponse





def get_user_location(request):
    print(request.META['HTTP_USER_AGENT'])
    remote_addr = request.META.get('HTTP_X_FORWARDED_FOR')
    if remote_addr:
        address = remote_addr.split(',')[-1].strip()
        print("if ", address)
    else:
        address = request.META.get('REMOTE_ADDR')
        print("else ", address)

    return HttpResponse("done")


