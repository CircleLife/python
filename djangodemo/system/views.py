from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse("欢迎登录")

def logout(reuqest):
    return HttpResponse("欢迎再次光临")