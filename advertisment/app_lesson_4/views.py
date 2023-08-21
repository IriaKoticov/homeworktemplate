from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement
from django.utils import timezone
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
    print([o.updated_at.strftime("%d.%m.%Y") for o in objectlist])
    print(timezone.now().date().strftime("%d.%m.%Y"))

    return HttpResponse("Сохр")

def post_ads(request):
    return render(request,"advertisement-post.html")

def registr(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")

def profile(request):
    return render(request,"profile.html")