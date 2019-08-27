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
	service = get_object_or_404(Services, pk=service_id)
	return render(request, 'services/detail.html', {'service': service})


def recent(request):
	latest_services = Services.objects.order_by('-pub_date')[:5]
	return render(request, 'services/recent.html', {'latest_services': latest_services})

	# output = ', '.join([q.title for q in latest_services])
	# return HttpResponse(output)

def detail_2(request):
	context = {
		
	}
	return render(request, 'services/detail_2.html', context)


def location(request):
	return HttpResponse("Here are the services closest to you... wait, actually we don't know how to do that yet.")

