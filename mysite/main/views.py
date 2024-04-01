from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from bs4 import BeautifulSoup
import requests
# Create your views here.

def index(response):
	return HttpResponse("<h1>First Django text </h1>")

def index2(response,id):
	ls = ToDoList.objects.get(id=id)
	return HttpResponse("<h1>First To-do list name %s</h1>" % ls.name)

def v1(response):
	return HttpResponse("<h1>Second Django text</h1>")

def v2(request):
	query = 'anxiety'
	url = f'https://psych2go.net/?s={query}&subset=posts&bp_search=1'
	r = requests.get(url) # get the page content using requests
	#print(r.content)
	soup = BeautifulSoup(r.text, 'html.parser') # parse the page HTML
	print(soup)

	test = [li.find('a') for li in soup.findAll('li', {'class': 'bp-search-item bp-search-item_post has-access'})]
	
	data = []
	for a in test:
		data.append(a['href'])

	#url = "https://jsearch.p.rapidapi.com/search"

	#querystring = {"query":"Python developer in San Diego, USA","page":"1","num_pages":"1"}

	# headers = {
	# 	"X-RapidAPI-Key": "be340b85c9mshc362df34fc85300p13a52ajsn9d9de6c5339e",
	# 	"X-RapidAPI-Host": "jsearch.p.rapidapi.com"
	# }

	#response = requests.get(url, headers=headers, params=querystring)

	#print(response.json())

	#details = response.json()

	#data = details['data']

	context = {
			'data': data
	}

	return render(request,'articles/v2.html',context)

def home(request):
	url = "https://jsearch.p.rapidapi.com/search"

	querystring = {"query":"Java developer in Los Angeles, USA","page":"1","num_pages":"1"}

	headers = {
		"X-RapidAPI-Key": "be340b85c9mshc362df34fc85300p13a52ajsn9d9de6c5339e",
		"X-RapidAPI-Host": "jsearch.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	#print(response.json())

	details = response.json()

	data = details['data']

	context = {
			'data': data
	}

	return render(request,'jobapi/home.html',context)
