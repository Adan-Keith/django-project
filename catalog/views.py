from django.shortcuts import render
#importing all model classes that we'll use to access data in all our views
from .models import Book, Author, BookInstance, Genre
# Create your views here.

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

