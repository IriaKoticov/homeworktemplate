from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,"index.html")

def top_sellers(request):
    return render(request,"top-sellers.html")

def post_ads(request):
    return render(request,"advertisement-post.html")

def registr(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")

def profile(request):
    return render(request,"profile.html")