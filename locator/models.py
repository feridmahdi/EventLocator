from django.db import models
import datetime
from django.urls import reverse

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200) #initial='Event Name',
    description = models.TextField() #label='Event Beschreibung'
    start_time = models.DateTimeField() #initial=datetime.date.today
    end_time = models.DateTimeField()
    image = models.ImageField(upload_to='images/',default='/media/images/default.jpg') # ,height_field=800,width_field=640
    def __str__(self):
        return self.title
    
    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<p>{self.title}</p><a href="{url}">edit</a>'

class Organizer(models.Model):
    name = models.CharField(max_length=100) # label='Organizer Name', 
    contactNumber = models.CharField(max_length=100) # label='Kontaktnummer', 
    email = models.EmailField() # label='Email', 
    url = models.URLField() #label='Webseite', initial='http://'
    description = models.CharField(max_length=100) # label='Weitere Informationen zum Organizer'
    image = models.ImageField()

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<p>{self.title}</p><a href="{url}">edit</a>'

class Address(models.Model):
    street = models.CharField(max_length=100)