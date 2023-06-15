from os import path, remove
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from .models import Blog, Comment

# Create your views here.
def homePage(request):
    # ! get all blog posts
    blogs = Blog.objects.all()

    # ! send all blog posts to the template
    context = {
        'blogs': blogs,
    }
    return render(request, 'base/home.html', context)

def loginPage(request):
    return render(request, 'base/login.html')

def signupPage(request):
    return render(request, 'base/signup.html')

def blogPage(request):
    blogs = Blog.objects.filter(user=request.user)
    context = {
        'blogs': blogs,
    }
    return render(request, 'base/blog.html', context)

@login_required(login_url='/login')
def blogAddPage(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        description = request.POST['description']
        featured_image = request.FILES['featured_image']
        fss = FileSystemStorage(location='static/assets/images', base_url='assets/images')
        filename = fss.save(featured_image.name, featured_image)
        uploaded_file_url = fss.url(filename)
        blog = Blog(title=title, description=description, featured_image=uploaded_file_url, user=request.user)
        blog.save()
        return redirect('/blog/' + str(blog.id))
    return render(request, 'base/blogAdd.html')

@login_required(login_url='/login')
def blogEditPage(request, pk):
    blog = Blog.objects.get(id=pk)
    if(request.method == 'POST'):
        title = request.POST['title']
        description = request.POST['description']
        featured_image = request.FILES['featured_image']
        if(featured_image):
            path.isfile('static/'+ str(blog.featured_image)) and remove('static/'+ str(blog.featured_image))
            fss = FileSystemStorage(location='static/assets/images', base_url='assets/images')
            filename = fss.save(featured_image.name, featured_image)
            uploaded_file_url = fss.url(filename)
            blog.featured_image = uploaded_file_url
        blog.title = title
        blog.description = description
        blog.save()
        return redirect('/blog/' + str(blog.id))
    context = {'pk': pk, 'title': blog.title, 'description': blog.description, 'featured_image': blog.featured_image}
    return render(request, 'base/blogEdit.html', context)

def blogDetails(request, pk):
    # ! get the blog post with the id=pk
    blog = Blog.objects.get(id=pk)
    if(request.method == 'POST'):
        comment_content = request.POST['comment'] # ! get the comment from the form
        comment = Comment(comment=comment_content, user=request.user, blog=blog)
        comment.save()
        return redirect('/blog/' + str(blog.id))
    comments = Comment.objects.filter(blog=blog)
    context = {'blog': blog, 'comments': comments}
    return render(request, 'base/blogDetails.html', context)

@login_required(login_url='/login')
def blogDelete(request, pk):
    blog = Blog.objects.get(id=pk)
    path.isfile('static/'+ str(blog.featured_image)) and remove('static/'+ str(blog.featured_image))
    blog.delete()
    return redirect('/blog')

@login_required(login_url='/login')
def commentDelete(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return redirect('/blog/' + str(comment.blog.id))

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
        
@login_required(login_url='/login')
def profilePage(request, pk):
    user = User.objects.get(id=pk)
    blogs = Blog.objects.filter(user=user)
    context = {'user': user, 'blogs': blogs}
    return render(request, 'base/profile/profile.html', context)

@login_required(login_url='/login')
def profileEditPage(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user = request.user
        user.username = username 
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return redirect('/profile/' + str(user.id))
    return render(request, 'base/profile/edit.html')
        
def logoutUser(request):
    logout(request)
    return redirect('/')

