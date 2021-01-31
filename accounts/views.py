from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from crudajax import views

def register(request):
    if request.method == 'POST':
        #get form values
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        #check if password matches
        if password == password2 :
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already taken')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username, password=password, email=email
                    ,first_name=first_name,last_name=last_name)
                    #Log in after register
                    # auth.login(request,user)
                    # messages.success(request,'Logged in Succefully')
                    # return redirect('index')
                    user.save()
                    messages.success(request,'You are now registerd, Log in Please')
                    return redirect('login')
        else:
            messages.error(request,'Password do not match')
            return redirect('register')

    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Logged in')
            return redirect('crud_ajax')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else :
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'Logged Out successfully')
        return redirect('crud_ajax')