from django.http import HttpResponse
from django.shortcuts import render

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
