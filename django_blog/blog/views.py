from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , authenticate, logout
from .forms import CustomUserCreationForm

#Homepage View
def home(request):
    
    return render(request, 'index.html')

#Registration page View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register/register.html', {'form': form})

#Login page view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            password = form.cleaned_data.get('password')
            user = authenticate(first_name=first_name, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with your desired redirect URL
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})  

#Logout page view
def logout_view(request):
    logout(request)
    return redirect('home') 

#Blog page View
def blog(request):
    
    return render(request, 'blog.html')