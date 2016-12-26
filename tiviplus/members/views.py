from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

from members.forms import LoginForm

def login_view(request):
	if request.method == "POST":
		form = LoginForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('planning:list-loan')
		return render(request, 'members/login.html',
				{ 'login_form': form,
				  'errors': ["N'a pas pu vous logger"]})
	else:
		form = LoginForm()
		return render(request, 'members/login.html',
				 { 'login_form': form })

@login_required
def logout_view(request):
	logout(request)
	redirect('members:login')
