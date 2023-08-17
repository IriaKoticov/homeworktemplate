from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement
# Create your views here.



def index(request):
    return render(request,"index.html")

def top_sellers(request):
    return render(request,"top-sellers.html")

def debug(request):
    #отладочная функция
    # for i in range(101):
    #     adv1 = Advertisement(
    #         title = f"тест{i}",
    #         text = f"текст{i}",
    #         author = "admin"
    #     )
    #     adv1.save()
    objectlist = Advertisement.objects.all()
    print([o for o in objectlist])

    return HttpResponse("Сохр")

def post_ads(request):
    return render(request,"advertisement-post.html")

def registr(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")

def profile(request):
    return render(request,"profile.html")