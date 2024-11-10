from django.shortcuts import render, redirect
from django.http import HttpResponse  
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return HttpResponse(f"<h1>Financials Home</h1> of {request.user.username}")  