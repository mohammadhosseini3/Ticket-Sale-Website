from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from accounts.models import profileModel
from .forms import *
from django.contrib.auth.models import User
# Create your views here.

def loginView(request):
    if request.method=='POST':
        username = request.POST.get('loginName')
        password = request.POST.get('loginPassword')

        # Authenticating username and password
        user = authenticate(request,username=username,password=password)
        
        # if it is successful it returns name of the user
        if user is not None:
            login(request,user)

            # user will be redirected to the requested page
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))

            # if url doesn't have 'next' parameter
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            messages.info(request,"نام کاربری یا رمز ورود اشتباه است")

    return render(request,'accounts/login.html',context={})

def logoutView(request):
    logout(request)
    return redirect('concert_app:concert_list')

@login_required
def profileView(request):
    profile = request.user.profile
    context = {
        'profile':profile
    }
    return render(request,'accounts/profile.html',context)

def registerView(request):
    RegisterForm = ProfileRegisterationForm()
    if request.method == 'POST':
        RegisterForm = ProfileRegisterationForm(request.POST,request.FILES)
        if RegisterForm.is_valid():
            # first we should create a user for registeration
            user = User.objects.create_user(
                first_name = RegisterForm.cleaned_data['first_name'],
                last_name = RegisterForm.cleaned_data['last_name'],
                email = RegisterForm.cleaned_data['email'],
                password = RegisterForm.cleaned_data['password'],
                username = RegisterForm.cleaned_data['username'],
            )
            user.save()

            # then we should make a profile for this user
            # we make an instance for profile
            profiel_model = profileModel(
                    user = user,
                    gender = RegisterForm.cleaned_data['gender'],
                    profile_img = RegisterForm.cleaned_data['profile_img'],
                    credit = RegisterForm.cleaned_data['credit'],
                )
            # saving instance model
            profiel_model.save()
            return redirect('accounts:login')

    context = {
        'RegisterForm':RegisterForm
    }
    return render(request,'accounts/register.html',context)

def ProfileEditView(request):
    if request.method == 'POST':
        profileEditForm = ProfileEditForm(request.POST,request.FILES,instance=request.user.profile)
        userEditForm = UserEditForm(request.POST,instance=request.user)
        if profileEditForm.is_valid() and userEditForm.is_valid():
            profileEditForm.save()
            userEditForm.save()
            return redirect('accounts:profile')
    else:
        profileEditForm = ProfileEditForm(instance=request.user.profile)
        userEditForm = UserEditForm(instance=request.user)
    context = {
        'profileEditForm':profileEditForm,
        'profileImg':request.user.profile.profile_img,
        'userEditForm':userEditForm
    }
    return render(request,'accounts/profile_edit.html',context)