
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='finance_home'),
]