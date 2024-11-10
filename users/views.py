from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            messages.success(request, f"Account created successfully for {user.username}!")
            return
    else:
        form = UserCreationForm()

    return render(request, "signup.html")

    