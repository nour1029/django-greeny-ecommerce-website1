from multiprocessing import context
import re
from django.shortcuts import render, redirect
from .forms import SignupForm, UserActivateForm
from .models import Profile, UserAdress, UserPhoneNumber
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
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


@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    numbers = UserPhoneNumber.objects.filter(user=request.user)
    user_adress = UserAdress.objects.filter(user=request.user)

    context = {'profile': profile, 'numbers': numbers, 'user_adress': user_adress, }
    return render(request, 'profile.html', context)


@login_required
def edit_profile(request):
    number_id = request.POST.get('number-id')
    address_id = request.POST.get('address-id')


    print(request.POST)
    print('-'*25)
    if number_id:
        phone_number = UserPhoneNumber.objects.get(user=request.user, pk=number_id)
        others_phone_numbers = UserPhoneNumber.objects.filter(user=request.user).exclude(id=number_id).update(active=False)
        phone_number.active = True
        phone_number.save()
        return JsonResponse({'result':'success'})

    if address_id:
        address = UserAdress.objects.get(user=request.user, pk=address_id)
        others_addresses = UserAdress.objects.filter(user=request.user).exclude(id=address_id).update(active=False)
        address.active = True
        address.save()
        return JsonResponse({'result':'success'})

def add_profile_number(request):
    type = request.POST.get('type')
    phone_number = request.POST.get('phone_number')
    user = request.user

    user_phone_number = UserPhoneNumber.objects.create(
        user = user,
        type = type,
        phone_number = phone_number
    )

    numbers = UserPhoneNumber.objects.filter(user=request.user)
    html = render_to_string('include/real-time/contact_numbers_section.html', {'numbers':numbers})
    return JsonResponse({'result':html})

def edit_profile_number(request):
    nubmer_id = request.POST.get('id')
    type = request.POST.get('type')
    phone_number = request.POST.get('phone_number')
    user = request.user


    user_phone_number = UserPhoneNumber.objects.get(user=user, pk=nubmer_id)

    user_phone_number.type = type
    user_phone_number.phone_number = phone_number
    user_phone_number.save()

    numbers = UserPhoneNumber.objects.filter(user=request.user)
    html = render_to_string('include/real-time/contact_numbers_section.html', {'numbers':numbers})
    return JsonResponse({'result':html})



def add_profile_address(request):
    pass


    



def wishlist(request):
    profile = Profile.objects.get(user=request.user)

    context = {'profile':profile}
    return render(request, 'wishlist.html', context)



