from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("You are in the home page")
    return render(request,'websites/index.html')

def about(request):
    # return HttpResponse("You are in the about page")
    return render(request,'websites/about.html')

def contact(request):
    # return HttpResponse("You are in the contact page")
    return render(request,'websites/contact.html')
