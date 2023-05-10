from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePage(request):
    return render(request, 'base/home.html')

def loginPage(request):
    return render(request, 'base/login.html')

def signupPage(request):
    return render(request, 'base/signup.html')