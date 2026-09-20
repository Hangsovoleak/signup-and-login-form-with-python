from django.conf import settings
from django.core.mail.message import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import get_template

from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from user.forms import UserRegisterForm, UserUpdateForm


# Profile
@login_required
def profile(request):

    if request.method == 'POST':

        form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Your profile has been updated successfully.'
            )

            return redirect('profile')

    else:

        form = UserUpdateForm(
            instance=request.user
        )

    return render(
        request,
        'user/profile.html',
        {
            'form': form,
            'title': 'My Profile'
        }
    )


# Index
def index(request):
    return render(request, 'user/index.html', {'title': 'index'})


# Register
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            # Send welcome email
            htmly = get_template('user/email.html')
            d = {'username': username}

            subject = 'Welcome'
            from_email = settings.EMAIL_HOST_USER

            html_content = htmly.render(d)

            msg = EmailMultiAlternatives(
                subject,
                html_content,
                from_email,
                [email]
            )

            msg.attach_alternative(html_content, "text/html")
            msg.send()

            # Account created successfully
            messages.success(
                request,
                'Your account has been created! You are now able to login.'
            )

            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(
        request,
        'user/register.html',
        {
            'form': form,
            'title': 'register here'
        }
    )


# Login
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():
            user = form.get_user()

            auth_login(request, user)

            messages.success(
                request,
                f'Welcome {user.username}!'
            )

            return redirect('index')

    else:
        form = AuthenticationForm()

    return render(
        request,
        'user/login.html',
        {
            'form': form,
            'title': 'Log in'
        }
    )