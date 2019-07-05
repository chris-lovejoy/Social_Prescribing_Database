from django.shortcuts import render, get_object_or_404
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

def detail(request, service_id):
	# return HttpResponse("Here is information on this service")


	service = get_object_or_404(Services, pk=service_id)
	return render(request, 'services/detail.html', {'service': service})


def recent(request):
	return HttpResponse("Here are the most recently-added services")

def location(request):
	return HttpResponse("Here are the services closest to you")

