from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import request

def index(request):
    return HttpResponse("Rango says, \"I am a Golden God!\"</br><a href='/rango/about/'>About</a>")
# Create your views here.

def about(request):
    return HttpResponse("Rango says, \"Here is the About Page\"</br><a href='/rango/'>Main</a>")