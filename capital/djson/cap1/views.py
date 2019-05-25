from django.shortcuts import render

from .models import Category

def categories (request):
	if request.method == 'POST':
		return "we got POST"

	else:
		return "we got GET"
