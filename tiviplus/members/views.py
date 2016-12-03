from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from members.forms import LoginForm

def login_view(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(user, request)
			return redirect(reverse('planning'))
		return render(request, 'members/login.html',
				 { 'login_form': form })
	else:
		form = LoginForm()
		return render(request, 'members/login.html',
				{ 'login_form': form })

@login_required
def logout_view(request):
	if request.user.is_authenticated:
		logout(user)
