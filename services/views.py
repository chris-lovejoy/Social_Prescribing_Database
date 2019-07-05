from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Services



def index(request):
	services = Services.objects.all()
	template = loader.get_template('services/index.html')
	context = {
		'services': services,
	}
	return HttpResponse(template.render(context,request))

    # return HttpResponse("Welcome. What services would you like to view?")


def recent(request):
	return HttpResponse("Here are the most recently-added services")

def location(request):
	return HttpResponse("Here are the services closest to you")

