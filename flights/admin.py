from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Flight, Airport, Passenger
# Register your models here.
#to customise the admin page
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration") #information to be seen when loading a flight

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport),
admin.site.register(Flight, FlightAdmin),
admin.site.register(Passenger, PassengerAdmin)
