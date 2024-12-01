from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from main.models import UserFormData
from .forms import CustomUserCreationForm, UserForm, CompetenciaFormSet, CustomAuthenticationForm


def landing_page(request):
    return render(request, 'main/landing_page.html')


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
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
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def user_form(request):
    try:
        user_form_data = UserFormData.objects.get(user=request.user)
    except UserFormData.DoesNotExist:
        user_form_data = None

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user_form_data)
        formset = CompetenciaFormSet(request.POST, instance=user_form_data)
        if form.is_valid() and formset.is_valid():
            user_form_data = form.save(commit=False)
            user_form_data.user = request.user
            user_form_data.save()
            formset.instance = user_form_data
            formset.save()
            return redirect('confirmation_page')
    else:
        form = UserForm(instance=user_form_data)
        formset = CompetenciaFormSet(instance=user_form_data)

    return render(request, 'main/user_form.html', {
        'form': form,
        'formset': formset,
    })


@login_required
def confirmation_page(request):
    return render(request, 'main/confirmation_page.html')
