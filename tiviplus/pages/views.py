from django.shortcuts import render, redirect

def home(request):
	if request.user.is_authenticated:
		return redirect('planning:list-loan')
	else:
		return redirect('login')

