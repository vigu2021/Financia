from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .forms import TransactionForm
from .models import Transaction

@login_required
def home(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)  
            transaction.user = request.user
            transaction.date_time = timezone.now()  
            transaction.save()
            return HttpResponse('<h1>Success!</h1>')  
    else:
        form = TransactionForm()
    
    # Fetch recent transactions
    recent_transactions = Transaction.objects.filter(user=request.user).order_by('-id')[:5]
    
    return render(request, 'transaction_form.html', {
        'form': form,
        'recent_transactions': recent_transactions
    })
