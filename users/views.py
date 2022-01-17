from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse

# Create your views here.
def index(request):#will be used to display infor of currently signed in user
    if not request.user.is_authenticated: #to tell if user is signed in or not
        return HttpResponseRedirect(reverse("login"))

    return render(request, "users/user.html")
    # return render(request, "flights/index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password) #if valid it gives back who the user is
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render (request, "users/login.html", {
                "message": "Invalid Credentials."
            })

    return render (request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })
    