from django.db import models

class Category (models.Model):
	num = models.IntegerField()
	parent = models.IntegerField()
	name = models.TextField()
