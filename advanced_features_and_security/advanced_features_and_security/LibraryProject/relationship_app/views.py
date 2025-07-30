from django.shortcuts import render, redirect
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def library_view(request):
    book = Book.objects.all() #Fetch all library instances from the database
    context = {'book_list': book}
    
    return render(request, 'relationship_app/list_books.html' , context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
            
        return render(request, 'relationship_app/register.html', {'form': form})
        
        
    
    

