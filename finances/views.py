
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm
from datetime import datetime



@login_required
def home(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.time = datetime.now()
            form.save()
            return HttpResponse('<h1>Success!</h1>')  
    else:
        form = TransactionForm()  
    return render(request, 'transaction_form.html', {'form': form})  # Pass the form to the template
