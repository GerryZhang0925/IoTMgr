from django.shortcuts import render
from DevMgr.forms import UserForm, UserOtherInfoForm

# Information from django
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'DevMgr/index.html')

@login_required
def user_list(request):
    return render(request, 'DevMgr/user.html')

@login_required
def plant_list(request):
    return render(request, 'DevMgr/plant.html')

@login_required
def data_list(request):
    return render(request, 'DevMgr/data.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        otherinfo_form = UserOtherInfoForm(data=request.POST)
        
        if user_form.is_valid() and otherinfo_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            other = otherinfo_form.save(commit=False)
            other.user = user
            other.save()

            registered = True

        else:
            print(user_form.errors, otherinfo_form.errors)

    else:
        user_form = UserForm()
        otherinfo_form = UserOtherInfoForm()

    return render(request, 'DevMgr/registration.html',
                  {'user_form':user_form,
                  'otherinfo_form':otherinfo_form,
                  'registered':registered})

def user_login(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
            
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")

    else:
        return render(request, 'DevMgr/login.html', {})
