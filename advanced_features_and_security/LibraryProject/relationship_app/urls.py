from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('library-function/', views.library_view, name='function-view'),
    path('library-class/', views.LibraryDetailView.as_view(), name='class-view'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name=''), name='logout'),
    path('register/', views.register, name='register'),
    
]