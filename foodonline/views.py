from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hi What the fuck are you doing")