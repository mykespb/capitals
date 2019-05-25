from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .models import Category

@csrf_exempt
def categories (request):
	if request.method == 'POST':
#		return HttpResponse("we got POST")
		return JsonResponse ({'method': 'POST', 'foo': 'bar'})

	else:
#		return HttpResponse("we got GET")
		return JsonResponse ({'method': 'GET', 'foo': 'bar'})
