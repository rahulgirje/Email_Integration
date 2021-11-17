from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages





def HomePageView(request):
    template_name = 'firstapp/home.html'
    return render(request,template_name)

def SignUpPageView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email Already Used")
            return redirect('signup')
        else:
            user = User.objects.create_user(username = email, password = password)
            user.save()
            send_mail('Sign In', f'You are Sign in using{email}','rahulgirje8897@gmail.com',[email])
            messages.success(request, f'Account Successfully Created {email}')
    template_name = 'firstapp/signup.html'
    return render(request,template_name)

def LoginView(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            messages.success(request, f'You  Log in  {u}')
            send_mail('Logged In', f'You have log in {u}','rahulgirje8897@gmail.com',[u])
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    template_name = 'firstapp/login.html'
    return render(request,template_name)

def LogoutView(request):
    logout(request)
    return redirect('home')
