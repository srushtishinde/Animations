from unicodedata import name
from animations.models import Animation
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime import date
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup(request):
    return render(request,'signup.html')

def loginn(request):
    return render(request,'login.html')

def about(request):
    return render(request, 'about.html')

def authenti(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            print('Username: ', username)
            user = auth.authenticate(username=username,password=password)
            print(user)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request,'Invalid Credentials!')
                return redirect('/login')
    return redirect('/login')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password1)
                user.save()
                print('User has been created')
                return render(request, 'login.html')
        else:
            messages.info(request,'Password not matching')
        return redirect('/signup')  
    else:
        return render(request, 'signup.html')

def index(request):
    return render(request, 'index.html',context={'animations': Animation.objects.all()})

def filter(request):
    type = request.POST['type']
    animations = Animation.objects.filter(type=type)
    m = {'animations': animations}
    return render(request,'filter.html', context=m)

def directory(request):
    return render(request, 'directory.html')

def added(request):
    if request.user.is_authenticated:
        username=request.POST['username']
        editor=request.POST['editor']
        editor1=request.POST['editor1']
        file01=request.FILES.get('file01',False)
        print(file01)
        type=request.POST['type']
        aname=request.POST['aname']
        if editor==editor1:
            messages.info(request,'Cannot allow same links')
        elif Animation.objects.filter(editor=editor,editor1=editor1,aname=aname,file01=file01).exists():
            messages.info(request,'Already exists in the database.')
        else:
            newAnimation = Animation(username=username,editor=editor,editor1=editor1,file01=file01,type=type,aname=aname)
            newAnimation.save()
            return redirect('/')
    return redirect('/directory')

def logout(request):
    auth.logout(request)
    return redirect('/')