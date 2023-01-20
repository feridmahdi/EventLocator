from django.db import models
import datetime
from django.urls import reverse

#format = ['Legacy','Modern','Pioneer','Commander','Draft','Pauper']
FORMAT_CHOICE = (
    ('legacy','Legacy'),
    ('modern', 'Modern'),
    ('pioneer','Pioneer'),
    ('commander','Commander'),
    ('pauper','Pauper'),
    ('draft','Draft'),
)
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200, default='Location and Date') #initial='Event Name',
    start_time = models.DateTimeField() #default=datetime.date.today
    end_time = models.DateTimeField() #default=datetime.date.today
    format = models.CharField(max_length=10, choices=FORMAT_CHOICE, default='legacy')
    eintritt = models.PositiveIntegerField(default=10)
    maxTeilnehmer = models.PositiveIntegerField(default=24)
    description = models.TextField(default='Allgemeine Beschreibung,\nAnfahrt, Verpflegung, Händler,...\nErwartete Teilnehmer, Rundenzahl.\nProxy Regelung, Preise...') #label='Event Beschreibung'
    image = models.ImageField(upload_to='images/',default='/images/default.jpg') # ,height_field=800,width_field=640
    def __str__(self):
        return self.title
    
    @property
    def get_html_url(self):
        #url = reverse('locator:event_edit', args=(self.id,))
        #return f'<a href="{url}"> {self.title} </a>'
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}">{self.title}</a>'
        #return f'<p>{self.title}</p><a href="{url}">edit</a>'

class Organizer(models.Model):
    name = models.CharField(max_length=100, default='Organizer Name') # unique='true'
    contactNumber = models.CharField(max_length=100) # label='Kontaktnummer', 
    email = models.EmailField(default='address@provider.com') # label='Email', 
    url = models.URLField(default='http://www.website.com') #
    description = models.TextField(default='Weitere Informationen zum Organizer') 
    image = models.ImageField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='organizer',blank=True, null=True)

class Address(models.Model):
    street = models.CharField(max_length=100)
    streetNr = models.PositiveIntegerField(default=1)
    city = models.CharField(max_length=100,default='Berlin')
    cityCode = models.PositiveIntegerField(default=1000)
    country = models.CharField(max_length=100,default='Germany')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='address',blank=True, null=True)
    
    def __str__(self):
        return self.street + ' ' + self.streetNr + ', ' + self.cityCode  + ' ' + self.city  + ', ' + self.country

# Search Database
class Search(models.Model):
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address