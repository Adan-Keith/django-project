from django.db import models
from django.urls import reverse #used to generate URLS by reversing the URL patterns
import uuid #Required forunique book instances

# Create your models here.
# class MyModelName(models.Model):
#     # A typical class defining a model derived from the model class
    
#     #Fields
#     my_field_name = models.CharField(max_length=20, help_text='Enter Field Documentation')
    
    
#     #Metadata
    
#     class Meta:
#         ordering = ['-my_fiel_name']
        
#     #Methods
#     def get_absolute_url(self):
#         # Retruens the URL to access a particular instance of MyModelName
#         return reverse("model_detail-view", args=[str(self.id)])
  
#     def __str__(self):
#         #string for representing the MyModelName object (in Admin Site etc.).
#         return self.my_field_name

class Genre(models.Model):
    #Model representing a book genre
    name = models.CharField(max_length=200, unique=True, help_text="Enter a book genre you wish to search (e.g. Scienec Fiction, French Poetry etc.)")
    
    def __str__(self):
        #String for representing models object
        return self.name
    
    def get_absolute_url(self):
        #Returns the url to access a particular genre instance
        return reverse("genre-detail", args=[str(self.id)])
    
    
class Book(models.Model):
    #model representing a book (but not a specific copy of a book)
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    #FK used because a book can only have ine author, but authors can have multiple books
    
    #Author as a string rather than nobject because it hasnt been declared yet in file
    
    summary = models.TextField(
        max_length=1000, help_text="Enter a brief deription of the book"
    )
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 cahracter <a href="https://www.isbn-international.org/content/what-isbn''">ISBN number</a>')
    
    #many to many field used because genre can contain many books. books can cover many genres
    #genre class has alreadt been defines so we specify the object above
    
    genre = models.ManyToManyField(
        Genre, help_text="select a genre for this book"
    )
    
    # LANGUAGE_CHOICES = (
    #     ('farsi', 'Farsi'),
    #     ('english', 'English'),
    #     ('spanish', 'Spanish'),
    #     ('german', 'German'),
    # )
    
    language = models.ForeignKey('Language', on_delete=models.RESTRICT, null=True)
    
    def __str__(self):
        #String representing the Model Object
        return self.title
    
    def get_absolute_url(self):
        #Returns the url to access a detailed record for this book
        return reverse("book-detail", args=[str(self.id)])
    
    def display_genre(self):
        #Creating a string for a genre. this is required to  display genre in the admin
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = 'Genre'
    
    
class BookInstance(models.Model):
    #Model representing a spwcific copy of a book(i.e that can be borrowed from the library)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across the whole librabry")
    
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text="Book Availability",
    )
    
class Meta:
    ordering = ['due_back']
    
    def __str__(self):
        #String representing the Model object
        return f'{self.id} ({self.book.title})'   
    
    def get_absolute_url(self):
        # Returns the URL to access a particular author instance
        return reverse('book-detail', args=[str(self.id)])

    
class Author(models.Model):
    #Model representing the author
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)    
    
    class Meta:
        ordering = ['last_name', 'first_name']
        
    def __str__(self):
        #String for representing the model object
        return f'{self.last_name}, {self.first_name}'
    def get_absolute_url(self):
        # Returns the URL to access a particular author instance
        return reverse('author-detail', args=[str(self.id)])

class Language(models.Model):
    #model representing different languages the books are written in
    name = models.CharField(max_length=100)
    
    def __str__(self):
         
        return self.name

