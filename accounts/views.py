from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import ProfileForm, UserForm
from .models import Profile


@login_required(login_url='login')
def index(request):
    return render(request, 'main/index.html')


def register_view(request):
    if request.method == 'POST':

        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 and password2 and password1 != password2:
            messages.error(request, 'Пароли не совпадают')
            return redirect('register')

        if user_form.is_valid() and profile_form.is_valid():
            try:
                user1 = User(
                    username=user_form.cleaned_data['username'],
                    email=user_form.cleaned_data['email'],
                )
                user1.set_password(password2)
                user1.save()

                profile = Profile(
                    image=profile_form.cleaned_data['image'],
                    phone=profile_form.cleaned_data['phone'],
                    user=user1)
                profile.save()
                messages.success(
                    request, f'Аккаунт для {user1.username} был успешно создан! Можете войти в систему')
                return redirect('login')

            except Exception:
                messages.error(request, 'Ошибка регистрации')
                return redirect('register')

        else:
            messages.warning(
                request, "Пожалуйста исправьте ошибки в форме регистрации")
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }

    return render(request, 'accounts/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/')

def login_view(request):
    if request.method == 'POST':
        #input username
        #input password

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Добро пожаловать {username}')
            return redirect('home')
        else:   
            messages.error(request, 'Неверный логин или пароль')
    return render(request, 'accounts/login.html')
