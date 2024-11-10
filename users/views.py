from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def home(request):
    return render(request,'home.html')

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            messages.success(request, f"Account created successfully for {user.username}!")
            return redirect('login')
    else:
        messages.error(request, "There was an error with your form.")

    return render(request, "signup.html")

    
