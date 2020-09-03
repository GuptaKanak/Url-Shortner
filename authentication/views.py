from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth

# Create your views here.

def logout(request):
	auth.logout(request)
	return redirect('/login')
def login(request):
	if not request.user.is_authenticated:
		pass
		if request.method=="POST":
		#handle login
			if request.POST['email'] and request.POST['password']:
				try:
					user=User.objects.get(email=request.POST['email'])
					auth.login(request,user)
					if request.POST['next']!='':
						return redirect(request.POST.get('next'))
					else:
						return redirect('/')
					return redirect('/')
				except User.DoesNotExist:
					return render(request,'login.html',{'error':'user DoesNotExist'})
			else:
				return render(request,'login.html',{'error':'emptyfields'})
		else:
			return render(request,'login.html')
	else:
		return redirect('/')	
def signup(request):
	if request.method=="POST":
		#handle sign in 
		if request.POST['password']==request.POST['password2']:
			if request.POST['username'] and request.POST['email'] and request.POST['password']:
				try:
					user=User.objects.get(email=request.POST['email'])
					return render(request,'signup.html',{"error":"user already exists"})
				except User.DoesNotExist:
					User.objects.create_user(
						username=request.POST['username'],
						email=request.POST['email'],
						password=request.POST['password'],
						)
					messages.success(request,"Signup Success, Login Here")
					return redirect(login)
			else:
				return render(request,'signup.html',{"error":"empty fields"})
		else:
			return render(request,'signup.html',{"error":"password's donot match"})
	else:		
		return render(request,'signup.html')