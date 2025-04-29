from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Book

def index(request):
    return render(request, "booking/index.html")

def booking_slot(request):
    return render(request, "booking/book_slot.html")

class BookDetailView(generic.DetailView):
    model = Book
    template_name= "booking/book_review.html"


