from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Book

def index(request):
    return render(request,"booking/index.html")

def booking_slot(request):
    return "book a slot"