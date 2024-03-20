from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm
from .models import MusicalEvent


# Create your views here.
# Create your views here.
# Home page
def index(request):
    # Fetch all MusicalEvent objects
    musical_events = MusicalEvent.objects.all()
    if 'district' in request.GET:
        district = request.GET['district']
        musical_events = musical_events.filter(district__icontains=district)    
    return render(request, 'index.html', {'musical_events': musical_events})

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

def user_base(request):
    return render(request,'base.html')

def my_view(request):
    # Fetch data stored by superuser
    superuser_data = MusicalEvent.objects.filter(user__is_superuser=True)
    return render(request, 'index.html', {'superuser_data': superuser_data})
