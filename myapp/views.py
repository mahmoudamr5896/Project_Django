from django.shortcuts import render 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Myuser
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    # return HttpResponse("Happy Day Mahmoud")
    return render(request, 'myapp/home.html')

def profile(request):
    return render(request, 'myapp/profile.html')


def signup(request):
    if request.method == 'GET':
        return render(request,'myapp/signup.html')
    
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        confpassword = request.POST['confpassword']
        phone = request.POST['phone']
        # profilepic = request.FILES['profile_pic']  # Use FILES instead of POST for file upload

        data=Myuser.objects.filter(email=email)
        if data:
            return render(request,'myapp/signup.html')
        
        User.objects.create_user(username=fname, email=email, password=password)
        Myuser.objects.create(fname=fname, lname=lname, email=email, password=password, phone=phone)

        return redirect("signin")
    

def signin(request):
    if request.method == 'GET':
        
        return render(request,'myapp/signin.html')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password=request.POST['password']
        
        data=Myuser.objects.filter(email=email)
        
        if data:
            auth = authenticate(username=data[0].email, password=password)
            
            if auth:
                login(request,auth)
                request.session["email"]=email
                return redirect ("profile")
            else:
                return render (request,'myapp/signin.html')   

        else:
            return render(request,'myapp/signin.html')
        

def signout(request):
    logout(request)
    return redirect('signin')