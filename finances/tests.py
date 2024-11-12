from django.test import TestCase
from django.utils import timezone
from .models import Transaction
from .utils import get_total_amount, get_all_comparisons
from django.contrib.auth.models import User

class TransactionTest(TestCase):  
    def setUp(self):  
        self.user = User.objects.create_user(username='username', password='password')
        self.now = timezone.now()

        Transaction.objects.create(user=self.user, amount=100, trans_type='ice', is_gain=True, date_time=self.now - timezone.timedelta(days=1))
        Transaction.objects.create(user=self.user, amount=50, trans_type='ice', is_gain=False , date_time=self.now - timezone.timedelta(days=1))
        Transaction.objects.create(user=self.user, amount=100, trans_type='ice', is_gain=True, date_time=self.now - timezone.timedelta(days=8))
        Transaction.objects.create(user=self.user, amount=150, trans_type='ice', is_gain=False, date_time=self.now - timezone.timedelta(days=28))
        Transaction.objects.create(user=self.user, amount=100, trans_type='ice', is_gain=True, date_time=self.now - timezone.timedelta(days=45))
        Transaction.objects.create(user=self.user, amount=150, trans_type='ice', is_gain=True, date_time=self.now - timezone.timedelta(days=230))
        Transaction.objects.create(user=self.user, amount=150, trans_type='ice', is_gain=True, date_time=self.now - timezone.timedelta(days=500))

    def test_sum(self):
        total_amount = get_total_amount(self.user)
        self.assertEqual(total_amount, 400)  
    
    def test_comparision(self):
        compare_7_days, compare_30_days, compare_365_days = get_all_comparisons(self.user)

        #Check the 7 days comparison
        self.assertEqual(compare_7_days['this_period_sum'], 50)   
        self.assertEqual(compare_7_days['last_period_sum'], 100)     
        # Check the 30-day comparison
        

        self.assertEqual(compare_30_days['this_period_sum'], 0) 
        self.assertEqual(compare_30_days['last_period_sum'], 100)    
        # Check the 365-day comparison
        self.assertEqual(compare_365_days['this_period_sum'], 250)  
        self.assertEqual(compare_365_days['last_period_sum'],150 )       

        

    



