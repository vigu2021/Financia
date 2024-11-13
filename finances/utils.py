from .models import Transaction
from django.utils import timezone
from datetime import timedelta

#Total amount in users balance (as of so far)
def get_total_amount(user):
    transactions =  Transaction.objects.filter(user=user)
    total_sum = find_sum(transactions)
    return total_sum


#Get all the comparisions that will be displayed 7,30 and 365 days
def get_all_comparisons(user):
    compare_7_days = get_period_comparision(user,7)
    compare_30_days = get_period_comparision(user,30)
    compare_365_days = get_period_comparision(user,365)

    return compare_7_days,compare_30_days,compare_365_days

#Helper function to get comparision sum of amounts of different periods.
def get_period_comparision(user,days):
    current_date_time = timezone.now()

    start_of_this_period = current_date_time - timedelta(days = days - 1)
    end_of_this_period = current_date_time

    start_of_prev_period = start_of_this_period - timedelta(days = days)
    end_of_prev_period =  start_of_this_period - timedelta(days = 1)


    #Get transaction of this period and the sum 
    this_period_transactions = Transaction.objects.filter(
        user = user,
        date_time__date__gte=start_of_this_period.date(), 
        date_time__date__lte=end_of_this_period.date(),
    )
    this_period_sum = find_sum(this_period_transactions)

    #Get transactions of previous period 
    last_period_transactions = Transaction.objects.filter(
        user = user,
        date_time__date__gte=start_of_prev_period.date(), 
        date_time__date__lte=end_of_prev_period.date(),
    )
    last_period_sum = find_sum(last_period_transactions)
    
    period_comparision  = this_period_sum - last_period_sum

    return {
        'this_period_sum' : this_period_sum,
        'last_period_sum' : last_period_sum ,
        'period_comparision': period_comparision
    }

#Helper function to sum of amounts in transaction table
def find_sum(table):
    total_sum = 0 
    for entry in table:
        if entry.is_gain:
            total_sum += entry.amount
        else:
            total_sum -= entry.amount
    return total_sum   




