from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# from .forms import UserRegistrationForm
# from workspace.views import welcome
# Create your views here.


# def register(request):
# 	if request.method == 'POST':
# 		form = UserRegistrationForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data.get('username')
# 			messages.success(request, f'Account created for {username}!')
# 			return redirect('landing_page')

# 	else:
# 		form = UserRegistrationForm()
# 	return render(request, 'account/signup.html', {'form' : form})


# def login_request(request):
# 	if request.method == 'POST':
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f'You are now logged in as {username}.')
# 				return redirect('main:homepage')
# 			else:
# 				messages.error(request,'Invalid username or password.')
# 		else:
# 			messages.error(request,'Invalid username or password.')
# 	form = AuthenticationForm()
# 	return render(request, 'account/login.html', {'login_form':form})


def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2:
            if (User.objects.filter(username=username).exists()):
                messages.warning(request,'User Name Already Exists')
                return redirect('signup')
            elif (User.objects.filter(email=email).exists()):
                messages.warning(request,'Email Already Exists')
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    password=password1,  
                    username=username, 
                    first_name=first_name, 
                    last_name=last_name, 
                    email=email,
                )
                user.save()
                messages.success(request,'User Created')
                return redirect('landing_page')
        else:
            messages.warning(request,'User Password MisMatching')
            return render(request, 'account/signup.html')
    else:
       return render(request, 'account/signup.html') 


def login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    if request.method == 'POST':
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('landing_page')

        else:
            messages.warning(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'account/login.html')
