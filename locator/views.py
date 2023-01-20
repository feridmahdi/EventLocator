# locator/views.py
#Calender Impl https://www.huiwenteo.com/normal/2018/07/29/django-calendar-ii.html
#Folium Impl: https://www.youtube.com/watch?v=2uFJ43DvhHg&t=434s
#Packages: geocoder, folium, django, django-crispy-forms

from datetime import datetime, date, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.conf import settings
from django.urls import reverse
from django.utils.safestring import mark_safe
from calendar import monthrange
import folium, geocoder
from django.contrib import messages

from .models import *
from .forms import EventForm , SearchForm
from .utils import Calendar

def home(request):
    return render(request, 'locator/osmap.html')

def osmap(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/osmap')
    else:
        form = SearchForm()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    if lat == None or lng == None:
        address.delete()
        address = Search.objects.all().last()
        location = geocoder.osm(address)
        lat = location.lat
        lng = location.lng
        messages.warning(request, 'Invalid Address')
    country = location.country
    # Create Map Object
    m = folium.Map(location=[50.95, 8.77], zoom_start = 6)
    # Create a Marker
    folium.Marker([lat, lng], tooltip='Search Loc', popup='search PopUp Text').add_to(m)
    
    folium.Marker([50.95, 8.77], tooltip='Hover Text', popup='PopUp Text').add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {    
        'm' : m,
        'form': form,
    }
    return render(request, 'locator/osmap.html', context)


class CalendarView(generic.ListView):
    model = Event
    template_name = 'locator/calendar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)
        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['calendar'] = mark_safe(html_cal)
        return context

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    cal = Calendar(d.year, d.month)
    days_in_month = monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.date.today()

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'locator/event.html', {'form': form})