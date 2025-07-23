from django.shortcuts import render
from .models import Library, Book
from django.views.generic import DetailView

def library_list(request):
    book = book.objects.all() #Fetch all library instances from the database
    context = {'book_list': book}
    
    return render(request, relationship_app/library_details.html , context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
        
        
    
    

