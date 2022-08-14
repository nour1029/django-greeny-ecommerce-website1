from multiprocessing import context
import re
from django.shortcuts import render, redirect
from .forms import SignupForm, UserActivateForm
from .models import Profile, UserAdress, UserPhoneNumber
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            myform = form.save(commit=False)
            myform.active = False
            myform.save()
            profile = Profile.objects.get(user__username=username)
            print(profile)
            print(profile.code)
            send_mail(
                subject='Activate your account',
                message=f'use this code {profile.code} to activate your account',
                from_email='nour.m7amad.ezeem@gmail.com',
                recipient_list=[email],
                fail_silently=False,
            )

            return redirect(f'/accounts/{username}/activate')
    else:
        form = SignupForm()

    context = {'form': form}
    return render(request, 'registration/signup.html', context)


def user_activate(request, username):
    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form = UserActivateForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if profile.code == code:
                profile.code_used = True
                profile.save()
                return redirect(f'/accounts/login')
    else:
        form = UserActivateForm()

    context = {'form': form}
    return render(request, 'registration/activate.html', context)


def profile(request):
    profile = Profile.objects.get(user=request.user)
    numbers = UserPhoneNumber.objects.filter(user=request.user)
    user_adress = UserAdress.objects.filter(user=request.user)

    context = {'profile': profile, 'numbers': numbers, 'user_adress': user_adress, }
    return render(request, 'profile.html', context)


def edit_profile(request):
    pass
