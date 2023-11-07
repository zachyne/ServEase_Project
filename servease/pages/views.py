from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForm

# For the services
from services.models import Category, Service


def landing_page(request, *args, **kwargs): #args, **kwargs
	# return HttpResponse("<h1>Hello World</h1>") #string of HTML code
	return render(request, "landing_page.html", {})

def logout_user(request):
	logout(request)
	return redirect('log_in')

def login_page(request): #args, **kwargs
	# return HttpResponse("<h1>Hello World</h1>") #string of HTML code
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		
		if user is not None:
			login(request, user)
			return redirect('browse')

		else:
			messages.info(request, 'Username OR Password is incorrect')
	
	context = {}
	return render(request, "login_page.html", context)


def signup_page(request): #args, **kwargs
	# return HttpResponse("<h1>Hello World</h1>") #string of HTML code
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user)

			return redirect('log_in')

	context = {"form": form}
	return render(request, "signup_page.html", context)

@login_required(login_url='log_in')
def main_page(request, *args, **kwargs): #args, **kwargs
# return HttpResponse("<h1>Hello World</h1>") #string of HTML code
	return render(request, "banner.html", {})


@login_required(login_url='log_in')
def browse_page(request):
	services = Service.objects.filter(is_sold=False)[0:6]
	categories = Category.objects.all()

	return render(request, 'browse.html', {
		'categories': categories,
		'services': services,
		})

def about(request, *args, **kwargs): #args, **kwargs
# return HttpResponse("<h1>Hello World</h1>") #string of HTML code
	return render(request, "about.html", {})


