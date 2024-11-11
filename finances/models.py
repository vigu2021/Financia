from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Transaction(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='transaction')
    amount = models.FloatField(default = 0)
    trans_type = models.CharField(max_length=50)
    is_gain = models.BooleanField()
    date_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'transactions'

    def __str__(self):
        return f"{self.user} - {"+" if self.is_gain else "-"}{self.amount} - {self.trans_type} - {self.date}"
    

