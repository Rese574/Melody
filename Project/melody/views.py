from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from .forms import *
from .models import *

# Create your views here.
# Bolabola - dashboard and song registration
# Sison - index or landing page and customer registration
class MelodyIndexView(View):
	def get(self, request):
		return render(request, 'melody/index.html')

class MelodyProductDashboardView(View):
	def get(self, request):
		songs = Song.objects.all()
		context={
			'songs' : songs,
		}
		return render(request, 'melody/productDashboard.html', context)
	def post(self, request):
		if request.method == 'POST':
			return render(request, 'melody/songRegister.html')

class MelodyCustomerDashboardView(View):
	def get(self, request):
		customers = Customer.objects.all()
		context = {
			'customers' : customers,
		}
		return render(request, 'melody/customerDashboard.html', context)

class MelodyCustomerRegistrationView(View):
	def get(self, request):
		return render(request, 'melody/customerRegister.html')
	def post(self, request):
		form = CustomerForm(request.POST)
		if form.is_valid():
			fname = request.POST.get("firstname")
			lname = request.POST.get("lastname")
			bday = request.POST.get("birthday")
			add = request.POST.get("address")
			email = request.POST.get("email")
			password = request.POST.get("password")
			contact = request.POST.get("contact")
			form = Customer(firstname = fname, lastname = lname, birthday = bday, address = add, email = email, password = password, contact = contact)
			form.save()
			return HttpResponse("Customer added")
		else:
			print(form.errors)
			return HttpResponse("Form is invalid")

class MelodySongRegistrationView(View):
	def get(self, request):
		return render(request, 'melody/songRegister.html')
	def post(self, request):
		form = SongForm(request.POST)
		# songTitle = request.POST.get("songtitle")
		# print(songTitle)
		# artists = request.POST.get("artist")
		# print(artists)	
		if form.is_valid():
			title = request.POST.get("songtitle")
			genre = request.POST.get("genre")
			artist = request.POST.get("artist")
			date = request.POST.get("dateRelease")
			producer = request.POST.get("producer")
			songwriter = request.POST.get("songwriter")
			form = Song(songtitle = title, genre = genre, artist = artist, dateRelease = date, producer = producer, songwriter = songwriter)
			form.save()
			return HttpResponse("Song has been added!!!")
		else:
			print(form.errors)
			return HttpResponse("Form is invalid")		