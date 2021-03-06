from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Category

@csrf_exempt
def categories (request, num=0):
	if request.method == 'POST':
		data = json.load (request)

		# if we allow only 1 load of data with POST
		dropdata ()
		numer.restart ()

		# if we allow many loads of data with POST
#		numer.rebase ()

		savedata (data)

#		return HttpResponse("we got POST")
#		return JsonResponse ({'method': 'POST', 'foo': 'bar'})
#		return JsonResponse (data = data)

	else:
#		return HttpResponse("we got GET")
#		return JsonResponse ({'method': 'GET', 'num': num})
		data = getdata (num)

	return JsonResponse (data)


class UniCounter:
	""" class for unique counters """

	def __init__ (self):
		self.num = 0

	@property
	def getnext (self):
		self.num += 1
		return self.num

	def restart (self):
		self.num = 0

	def rebase (self):
		if Category.objects.count ():
			self.num = Category.objects.last().id

numer = UniCounter ()


def dropdata ():
	""" clear all data from DB """

	Category.objects.all().delete()


def savedata (data, parentid=0):
	""" store json data in database """

	# check for existance of data in DB:
	if Category.objects.filter (name=data ['name']) .exists ():
		return

	# write data to DB if OK: ...
	mynum = numer.getnext
	record = Category (num=mynum, parent=parentid, name=data ['name'])
	record.save()

	if "children" in data:
		for child in data ["children"]:
			savedata (child, mynum)

def getdata (num):
	""" extract and show needed data """

	data = {}
	node = Category.objects.get (num=num)

	if not node:
		return {}

	data ["num"] = node.num
	data ["name"] = node.name
	myparent = node.parent

	# get parents
	parents = []
	test = node
	while test.parent:
		test = Category.objects.get (num=test.parent)
		parents += [{"id": test.num, "name": test.name}]
	data ["parents"] = parents

	# get children
	children = []
	for test in Category.objects.filter (parent=num):
		children += [{"id": test.num, "name": test.name}]
	data ["children"] = children

	# get siblings
	siblings = []
	for test in Category.objects.filter (parent=myparent):
		if test.num == num:
			continue
		siblings += [{"id": test.num, "name": test.name}]
	data ["siblings"] = siblings

	return data

