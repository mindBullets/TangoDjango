from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import request

def index(request):
    return HttpResponse("Rango says, \"I am a Golden God!\"")
# Create your views here.
