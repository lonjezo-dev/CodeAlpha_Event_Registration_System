from django.contrib.auth import authenticate, login 
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

def register(request):
       if request.method == 'POST':
           form = CustomUserCreationForm(request.POST)
           if form.is_valid():
               user = form.save(commit=True)
               user.save()
               messages.success(request, 'Registration successful! Please check your email to activate your account.')
               return redirect('login')  # Redirect to the login page
       else:
           form = CustomUserCreationForm()
       return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Check if user exists first
            if not CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Account not found. Please register first.")
                return redirect('accounts:register')

            # User exists, now check password
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('events:index')
            else:
                messages.error(request, "Incorrect password. Please try again.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})