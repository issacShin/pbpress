from django.shortcuts import render
from .models import Book

# Create your views here.
def book_list(request):
    books = Book.objects.order_by('published_date')
    return render(request, 'book/index.html', {'books': books})