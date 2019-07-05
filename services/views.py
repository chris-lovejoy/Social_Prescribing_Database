from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome. What services would you like to view?")


def recent(request):
	return HttpResponse("Here are the most recently-added services")

def location(request):
	return HttpResponse("Here are the services closest to you")

