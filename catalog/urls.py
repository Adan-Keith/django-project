from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('book/<int:pk>/', views.book_detail, name='book-detail'),
]
