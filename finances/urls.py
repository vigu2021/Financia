
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='finance_home'),
    path('delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction')
]