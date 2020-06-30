from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    user = User.objects.all()
    location = Location.objects.all()
    total_users = user.count()
    total_locations = location.count()

    context = {'user': user, 'location': location, 'total_users': total_users, 'total_locations': total_locations}
    return render(request, 'accounts/dashboard.html', context)

def location(request):
    location = Location.objects.all()
    return render(request, 'accounts/location.html', {'location' :location})

def user(request):
    return render(request, 'accounts/user.html')
