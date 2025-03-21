from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import User
from .forms import UserRegisterForm


# Create your views here.


def register_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"You are already logged in.")
        return redirect("account:account")

    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data['username']

            messages.success(request, f'Account created for {username}! You are now able to log in.')

            new_user = authenticate(
                username = form.cleaned_data['email'],
                password = form.cleaned_data['password1'],
            )

            login(request, new_user)
            return redirect("account:account")
        

    else:
        
        form = UserRegisterForm()

    context = {
        'form': form,
    }

    return render(request,'userauths/sign-up.html', context)
