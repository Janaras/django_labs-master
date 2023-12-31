cdfrom django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.

def books_view(request):
    book_value = models.Book.objects.all()
    return render(request, "books.html",{"book_key":book_value})

def book_detail_view(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html', {'book_key': book_id})