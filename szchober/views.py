from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User 
from szchober.models import UserProfile
from szchober.forms import UserForm, UserProfileForm

from django.contrib.auth import authenticate, login 
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect


def index(request):
    return render(request, 'szchober/index.html')

def sign_up(request):
    return HttpResponse("sign up page - become a driver/rider")

def become_rider(request):
    return HttpResponse("sign up subpage - become a rider")

def become_driver(request):
    return HttpResponse("sign up subpage - become a driver")

def myAccount_rider(request):
    return HttpResponse("this is my rider account")

def myAccount_driver(request):
    return HttpResponse("this is my driver account")

def find_lift(request):
    return render(request, 'szchober/find-a-lift.html')

def about(request):
    return HttpResponse("the about page")

def feedback(request):
    return HttpResponse("the feedback page")


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            
            profile.save()
            registered = True
        
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    
    return render(request, 
                    'szchober/register.html',
                    context = {'user_form': user_form,
                                'profile_form': profile_form,
                                'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('szchober:index'))
            else:
                return HttpResponse("Your account is disabled")
        else:
            print("Invalid login details")
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'szchober/login.html')

