from django.http import HttpResponse


def printname(request):
    return HttpResponse("Hello Yoonsuh!")