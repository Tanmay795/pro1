from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import redirect


def home(request):
    return render(request, 'users/home.html')

def register(request):
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('Username')
                messages.success(request, f'Hi {username}, you have been signed up')
            return redirect('login')

        else:
            form = UserRegisterForm()

        return render(request, 'users/register.html',{'form': form})

def profile(request):
    return render(request, 'users/profile.html')
