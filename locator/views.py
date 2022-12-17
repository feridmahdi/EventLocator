
import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    return render(
        request,
        'locator/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def map_view(request):
    context = {
        "google_api_key": settings.GOOGLE_API_KEY,
    }
    return render(request, 'locator/map.html', context)
