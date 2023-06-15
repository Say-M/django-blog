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
    path('blog/delete/<str:pk>/', views.blogDelete),
    path('comment/delete/<str:pk>/', views.commentDelete),
    path('create-user/', views.createUser),
    path('login-user/', views.loginUser),
    path('profile/edit/', views.profileEditPage),
    path('profile/<str:pk>/', views.profilePage),
    path('logout/', views.logoutUser),
]
