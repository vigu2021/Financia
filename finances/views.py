from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.utils import timezone
from .forms import TransactionForm
from .models import Transaction
from .utils import get_total_amount,get_all_comparisons
from django.shortcuts import get_object_or_404


@login_required
def home(request):
    current_user = request.user   #Get user from request 
    if request.method == 'POST':
        form = TransactionForm(request.POST)

        #Check if amount is less 0 if so, flag an error:
        amount = request.POST.get('amount')
        if amount is None or float(amount) <= 0:
            form.add_error('amount', "The amount must be greater than 0.") 

        elif form.is_valid():
            transaction = form.save(commit=False)  #To prevent form saving to database without additional entries not in form(user,datetime)
            transaction.user = current_user
            transaction.date_time = timezone.now()  
            transaction.save()
            return redirect('finance_home')
    else:
        form = TransactionForm()
    
    # Fetch recent transactions
    recent_transactions = Transaction.objects.filter(user=current_user).order_by('-id')[:5]
    total_amount = get_total_amount(current_user)
    compare_7_days,compare_30_days,compare_365_days = get_all_comparisons(current_user) #This needs fixing 

    compare_7_days = compare_7_days['period_comparision']
    compare_30_days = compare_30_days['period_comparision']
    compare_365_days = compare_365_days['period_comparision']

    return render(request, 'transaction_form.html', {
        'form': form,
        'recent_transactions': recent_transactions,
        'total_amount':total_amount,
        'compare_7_days':compare_7_days,
        'compare_30_days':compare_30_days,
        'compare_365_days':compare_365_days
    })

@login_required 
def delete_transaction(request,transaction_id):
    transaction = get_object_or_404(Transaction,id=transaction_id, user=request.user)
    transaction.delete()
    return redirect('finance_home')

@login_required
def view_all_transactions(request):
    table = Transaction.objects.filter(user=request.user).order_by('-date_time')
    return render(request, 'transaction_list.html', {
        'transactions': table,
    })
