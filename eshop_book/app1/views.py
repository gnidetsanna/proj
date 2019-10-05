
from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
# Create your views here.

def index(request):
    ctx = {}
    ctx['a'] = 45
    ctx['some_value'] = 'value'
    all_books = Book.objects.all() #'SELECT * FROM app1_book;'
    ctx['all_books'] = all_books
    # print(all_books)
    for book in all_books:
        print(book.title)
    return render(request , 'index.html', ctx)


def calc(request):
    return render(request , 'calculator.html', {})


def about(request):
    return render(request , 'about.html', {})