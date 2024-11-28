from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import UserForm

def landing_page(request):
    return render(request, 'main/landing_page.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Log the user in after signup
            from django.contrib.auth import login, authenticate
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('form_page')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_form_data = form.save(commit=False)
            user_form_data.user = request.user
            user_form_data.save()
            return redirect('confirmation_page')
    else:
        form = UserForm()
    return render(request, 'main/user_form.html', {'form': form})

@login_required
def confirmation_page(request):
    return render(request, 'main/confirmation_page.html')