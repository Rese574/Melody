from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from .forms import *
from .models import *

# Create your views here.
# Bolabola - dashboard and song registration
# Sison - index or landing page and customer registration
class MelodyIndexView(View):
	def get(self, request):
		return render(request, 'melody/index.html')

class MelodyProductDashboardView(View):
	def is_valid_queryparam(param):
		return param != '' and param is not None

		if is_valid_queryparam(productDateMin):
			songs = songs.filter(date__gte=productDateMin)

		if is_valid_queryparam(productDateMax):
			songs = songs.filter(date__lt=productDateMax)

	def get(self, request):
		songs = Song.objects.all()
		context={
			'songs' : songs,
		}
		return render(request, 'melody/productDashboard.html', context)
	def post(self, request):
		if request.method == 'POST':
			if 'btnUpdate' in request.POST:
				sid = request.POST.get("song-id")
				title = request.POST.get("song-title")
				date = request.POST.get("song-release")
				print(date)
				artist = request.POST.get("song-artists")
				genre = request.POST.get("song-genre")
				writers = request.POST.get("song-writer")
				producer = request.POST.get("song-producer")
				update_song = Song.objects.filter(id = sid).update(songtitle = title, genre = genre, artist = artist, dateRelease = date, producer = producer, songwriter = writers)
				print(update_song)
			elif 'btnDelete' in request.POST:
				sid = request.POST.get("song-id")
				song = Song.objects.filter(id = sid).delete()
				print('record deleted')
			return redirect('melody:melody_productDashboard_view')

class MelodyCustomerDashboardView(View):
	def is_valid_queryparam(param):
		return param != '' and param is not None

		if is_valid_queryparam(customerateMin):
			customers = customers.filter(date__gte=customerDateMin)

		if is_valid_queryparam(customerDateMax):
			customers = customers.filter(date__lt=customerDateMax)

	def get(self, request):
		customers = Customer.objects.all()
		context = {
			'customers' : customers,
		}
		return render(request, 'melody/customerDashboard.html', context)
	def post(self, request):
		if request.method == 'POST':
			if 'btnUpdate' in request.POST:
				cid = request.POST.get("customer-id")
				fname = request.POST.get("customer-fname")
				lname = request.POST.get("customer-lname")
				date = request.POST.get("customer-bday")
				print(date)
				add = request.POST.get("customer-add")
				email = request.POST.get("customer-email")
				contact = request.POST.get("customer-contact")
				update_customer = Customer.objects.filter(id = cid).update(firstname = fname, lastname = lname, birthday = date, address = add, email = email, contact = contact)
				print(update_customer)
			elif 'btnDelete' in request.POST:
				cid = request.POST.get("customer-id")
				customer = Customer.objects.filter(id = cid).delete()
				print('record deleted')
			return redirect('melody:melody_customerDashboard_view')

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
			return redirect('melody:melody_customerDashboard_view')
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
			return redirect('melody:melody_productDashboard_view')
		else:
			print(form.errors)
			return HttpResponse("Form is invalid")		