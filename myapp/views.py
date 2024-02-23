from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Happy Day Mahmoud")
    return render(request, 'myapp/home.html')


def login(request):
    return render(request, 'myapp/sighnup.html')

def sighup(request):
    return render(request, 'myapp/signin.html')
