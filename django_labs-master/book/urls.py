from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books_view),
    path('book_detail/<int:id>/', views.book_detail_view),
]