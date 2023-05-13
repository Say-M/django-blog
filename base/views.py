from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def homePage(request):
    return render(request, 'base/home.html')

def loginPage(request):
    return render(request, 'base/login.html')

def signupPage(request):
    return render(request, 'base/signup.html')

def blogPage(request):
    return render(request, 'base/blog.html')

def blogAddPage(request):
    return render(request, 'base/blogAdd.html')

def blogEditPage(request, pk):
    return render(request, 'base/blogEdit.html')

def blogDetails(request, pk):
    context = {'pk': pk, 'title': 'Blog Details'}
    return render(request, 'base/blogDetails.html', context)

def createUser(request):
    if(request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password)
        user.save()
        return redirect('/login')
    
def loginUser(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if(user is None):
            return redirect('/login')
        else:
            login(request, user)
            return redirect('/')
        
def logoutUser(request):
    logout(request)
    return redirect('/')