from django.shortcuts import render
#importing all model classes that we'll use to access data in all our views
from .models import Book, Author, BookInstance, Genre
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.models import BookInstance
from django.views import generic
# Create your views here.

@login_required
def index(request):
    #View function of our home page
    
    #Generate counts of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1    
    #Available books (available status)
    num_instances_available = BookInstance.objects.filter(status='a').count()
    
    #the 'all()' is implified by defauly
    num_authors = Author.objects.count()
    
    word = "life"
    num_books_with_word = Book.objects.filter(title__contains=word).count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
        'num_books_with_word': num_books_with_word,
    }   

    #Render the HTML tempalte index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user, status='o').order_by('due_back')
            
            
import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from catalog.forms import RenewBookForm


# catalog/views.py

from django.shortcuts import render
from .models import Book

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'catalog/book_detail.html', {'book': book})


@login_required
@permission_required
def renew_book_librarian(request, pk):
    #View function for renewing a specific bookinstance by librarian
    book_instance = get_object_or_404(BookInstance, pk=pk)#????????????ADDED LATER< CHECK TO SE IF IT WORKS
    #if this is a POST request then process the Form data
    if request.method == 'POST':
        
        #Create a form instance and populate it with data from the request (binding)
        form = RenewBookForm(request.POST)
        
        #check if the form is valid
        if form.is_valid():
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()
            
            #redirect to a new url
            return HttpResponseRedirect(reverse('all-borrowed'))
        
        #and if this is a GET or any other method , create a default form
        else:
            proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
            form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
            
            context = {
                
                'form': form,
                'book_instance': book_instance,
                
            }
            return render(request, 'catalog/book_renew_librarian.html', context)