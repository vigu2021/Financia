from .models import Transaction
import plotly.express as px
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta

# Get transaction of specific time periods 
def get_transactions_time_period(user,time_period):
    today = timezone.now()
    if time_period == 'all_time':
        return Transaction.objects.filter(user = user)
    elif time_period == 'year':
        return Transaction.objects.filter(user = user,date__year = today.year)
    elif time_period == 'month':
        return Transaction.objects.filter(user = user,date__year = today.year, date__month = today.month)
    else:
        start_of_week = today - timedelta(days=today.weekday())
        return Transaction.objects.filter(user=user, date__gte=start_of_week)

def get_transaction_sum_by_time_period(user, time_period):
    today = timezone.now()


def pie_chart_by_category(user,time_period):
    transactions_all = get_transactions_time_period(user,time_period)
    data = transactions_all.values('trans_type').annotate(total_amount=Sum('amount'))
    
    categories = [item['trans_type'] for item in data]
    amount =  [item['total_amount'] for item in data]

    pie_chart = px.pie(names=categories,values=amount,title = 'Categories of spending')

    return pie_chart 

    



    

    

