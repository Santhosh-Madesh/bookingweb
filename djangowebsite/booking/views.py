from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Slot

def index(request):
    return render(request, "booking/index.html")

def booking_slot(request):
    return render(request, "booking/book_slot.html") 

class BookDetailView(generic.DetailView):
    template_name= "booking/book_review.html"
    
def DetailView(request, pk):
    data = request.POST["slot"]
    render(request, "booking/book_review.html",data)


