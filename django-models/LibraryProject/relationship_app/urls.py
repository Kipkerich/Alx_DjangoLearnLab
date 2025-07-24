from django.urls import path
from . import views
from .views import list_books
urlpatterns = [
    path('library-function/', views.library_view, name='function-view'),
    path('library-class/', views.LibraryDetailView.as_view(), name='class-view'),
]