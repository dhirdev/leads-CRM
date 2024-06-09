from django.shortcuts import render
from django.http import request
from .models import Lead, User, Buyer, Supplier, Agent, Campaign

def landing_page(request):
    return render(request, 'base.html')