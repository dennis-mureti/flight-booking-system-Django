from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger
# Create your views here.
def index (request):
    return render ( request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id) #to get the flight according to ID
    return render(request, "flights/flight.html", { #pass data to flight.html
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all() #to exclude passenger who are not on the flight. will help to register non passengers
    })

def book(request, flight_id): #request flight ID
    if request.method == "POST": #if request method is POST then we will perform a certain typeof action
        flight = Flight.objects.get(pk=flight_id) #get flight with flight ID
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"])) #the data of whose passenger ID we want is going to be passed by a form whose feild is passenger. int()-> to convertt into integer
        passenger.flights.add(flight) #to add new row into table of keeping track of passengers in flight
        return HttpResponseRedirect(reverse("flight", args=(flight.id,))) #reverse takes name of particular view and get the actual URL path

