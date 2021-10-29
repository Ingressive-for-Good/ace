from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import UserUpdateForm, ProfileUpdateForm


from .models import Profile


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


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'account/profile.html', context)

def logout_view(request):
    logout(request)
    return redirect('landing_page')