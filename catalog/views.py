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
            