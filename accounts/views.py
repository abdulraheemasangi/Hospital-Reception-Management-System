from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.


def login_(request):
    if request.method=='POST':
        username_data=request.POST['username']
        password_data=request.POST['password']
        u=authenticate(username=username_data,password=password_data)
        print(u)
        if u is not None:
            login(request,u)
            return redirect('home')
        else:
            wc=True
            return render(request,'login_.html',{'wc':wc})

 
    return render(request,'login_.html')

def register_(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        
        try:
            u=User.objects.get(username=username)
            return render(request,'register_.html',{'u':u})
        
        except:

            print(firstname,lastname,email,username,password)
            u=User.objects.create(first_name=firstname,last_name=lastname,email=email,username=username)
            u.set_password(password)
            u.save()
            return redirect('login_')
        
    return render(request,'register_.html')


def logout_(request):
    logout(request)  

    return redirect('login_')


@login_required(login_url='login_')
def profile(request):

    return render(request,'profile.html')


@login_required(login_url='login_')
def changepass(request):

    if request.method=='POST':
        np=request.POST['password']
        user=User.objects.get(username=request.user)
        user.set_password(np)
        user.save()
        return redirect('login_')

    return render(request,'changepass.html')


@login_required(login_url='login_')
def update_profile(request):
    
    user = request.user

    if request.method == 'POST':
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']

        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')  

    return render(request, 'update_profile.html', {'user': user})