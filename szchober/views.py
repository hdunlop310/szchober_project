from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world! this is the home page!!")

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
    return HttpResponse("find lift page")

def about(request):
    return HttpResponse("the about page")

def feedback(request):
    return HttpResponse("the feedback page")
