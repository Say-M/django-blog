from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage),
    path('login/', views.loginPage),
    path('signup/', views.signupPage),
    path('blog/', views.blogPage),
    path('blog/add/', views.blogAddPage),
    path('blog/<str:pk>/', views.blogDetails),
    path('blog/edit/<str:pk>/', views.blogEditPage),
    path('create-user/', views.createUser),
    path('login-user/', views.loginUser),
    path('logout/', views.logoutUser),
    path('create-blog/', views.createBlog),
]
