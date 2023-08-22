from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement
from django.utils import timezone
# Create your views here.



def index(request):
    advlist = Advertisement.objects.all()
    context = {"advertisment" : advlist }
    return render(request,"index.html",context = context)

def top_sellers(request):
    return render(request,"top-sellers.html")

def debug(request):

    objectlist = Advertisement.objects.all()

    return HttpResponse("Сохр")

def post_ads(request):
    return render(request,"advertisement-post.html")

def registr(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")

def profile(request):
    return render(request,"profile.html")