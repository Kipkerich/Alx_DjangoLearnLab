from django.urls import path
from . import views

urlpatterns =[
    path('home/', views.home, name='home'),
    path('blog/', views.blog, name='posts'),
    path('register/', views.home, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
]