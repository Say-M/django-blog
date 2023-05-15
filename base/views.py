from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Blog

# Create your views here.
def homePage(request):
    blogs = Blog.objects.all()[:9]
    context = {
        'blogs': blogs,
    }
    print(blogs)
    return render(request, 'base/home.html', context)

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
    blog = Blog.objects.get(id=pk)
    blog.created_at
    context = {'pk': pk, 'title': blog.title, 'description': blog.description, 'featured_image': blog.featured_image, 'user': blog.user}
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
            messages.error(request, 'Invalid Credentials')
            return redirect('/login')
        else:
            login(request, user)
            return redirect('/')
        
def logoutUser(request):
    logout(request)
    return redirect('/')


def createBlog(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        description= request.POST['description']
        # featured_image = request.POST['featured_image']
        print(title, description)
        blog = Blog(title=title, description=description, user=request.user)
        blog.save()
        return redirect('/blog')
