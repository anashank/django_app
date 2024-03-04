from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(response):
	return HttpResponse("<h1>First Django text </h1>")

def index2(response,id):
	ls = ToDoList.objects.get(id=id)
	return HttpResponse("<h1>First To-do list name %s</h1>" % ls.name)

def v1(response):
	return HttpResponse("<h1>Second Django text</h1>")