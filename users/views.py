from django.shortcuts import render, redirect

from users.forms import RegisterForm


# Create your views here.

def home(request):
    return render(request, 'users/index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', context={'form': form})

