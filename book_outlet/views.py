
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Book
from django.db.models import Avg

# Create your views here.

def index(request):
    books =  Book.objects.all()
    number_of_books = books.count()
    avarage_rating = books.aggregate(Avg("rating"))
    return render(request,"book_outlet/index.html",{"books":books,
    "number_of_books":number_of_books,
    "avarage_rating":avarage_rating
    })

def details(request,slug):
    book =  get_object_or_404(Book,slug=slug)
    return render(request,"book_outlet/book_detail.html",{"book":book,
    })
