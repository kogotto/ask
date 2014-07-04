from django.shortcuts import render
from djungo.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world")
