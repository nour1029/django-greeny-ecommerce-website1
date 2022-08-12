from multiprocessing import context
from django.shortcuts import render
from .forms import SignupForm
from .models import Profile
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
    else:
        form = SignupForm()

    context = {'form': form}
    return render(request, 'registration/signup.html', context)


def profile(request):
    pass


def edit_profile(request):
    pass
