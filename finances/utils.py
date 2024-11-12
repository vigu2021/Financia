from .models import Transaction
from django.db.models import Sum

#Get total sum from database
def get_total_amount(user):
    transactions =  Transaction.objects.filter(user=user)
    total_sum = 0 
    for entry in transactions:
        if entry.is_gain:
            total_sum += entry.amount
        else:
            total_sum -= entry.amount
    return total_sum    




