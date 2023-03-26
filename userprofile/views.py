from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from .forms import ProfileUserForm, NewuserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def home(request):
	return render(request, 'home.html', {})

def settings(request, user_id):
	if request.user is not None:
		if request.method == 'POST':
			form = ProfileUserForm(request.POST, request.FILES or None, instance=request.user.profile)
			if form.is_valid():
				form.save()
				return redirect("home")
			else:
				print("not valid form!!")
		form = ProfileUserForm()
	else:
		print("user not authenticated!!")
	return render(request, 'userprofile/settings.html', {'form': form})

def user_logout(request, user_id):
	logout(request)
	# Return to homepage.
	return redirect("home")

def user_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="userprofile/login.html", context={"login_form": form})



def register_user(request):
	if request.method == "POST":
		form = NewuserForm(request.POST, request.GET or None)
		if form.is_valid():
		   form.save()
		   username = form.cleaned_data.get('username')
		   raw_password = form.cleaned_data.get('password1')
		   user = authenticate(username=username, password=raw_password)
		   login(request, user)
		   return redirect('home')
		else:
		   messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewuserForm()
	return render (request, "userprofile/register.html", context={"register_form":form})

# Create your views here.