
from django.urls import path
from . import views

urlpatterns = [
    
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('profile/', views.profile_view, name='profile'),
    
    path('post/new/' , views.create_posts, name='create_post'),
    path('post/<int:pk>/', views.view_posts, name='view_posts'),
    path('post/<int:pk>/update/', views.update_posts, name='edit_posts'),
    path('post/<int:pk>/delete/', views.delete_posts, name='delete_posts'),

]