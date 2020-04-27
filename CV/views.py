from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from CV.forms import UserForm, ProfileForm
# Create your views here.
from CV.models import Profile


def home(request):
    # try:
    #     #     if request.user.id is not None:
    #     #         profile = Profile.objects.get(id=request.user.id)
    #     # except:
    #     #     return render(request, 'CV/createprofile.html', context)
    context = {'title': 'Test Home Page '}
    return render(request, 'CV/profile.html', context)


def CreateProfile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'CV/createprofile.html', context)


def registerPage(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(
                request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'CV/register.html', context)


def EditProfile(request, id):
    print('DFFFFFFFFFFFFFFFFFFFf', request.user)
    profile = Profile.objects.get(id=id)
    form = ProfileForm(instance=profile)

    context = {}
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        return render(request, 'CV/createprofile.html', context)
    context['form'] = form
    return render(request, 'CV/createprofile.html', context)


def DeleteProfile(request, id):
    profile = Profile.objects.get(id=id)
    profile.delete()
    request.user.delete()
    return redirect('login')


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'CV/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
