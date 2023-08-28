from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement
# from .forms import Advforms
# Create your views here.
from .models import Advmodelform


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

    if request.method == "POST":
        form = Advmodelform(request.POST,request.FILES)
        if form.is_valid():
            adv_obj = Advertisement(**form.cleaned_data)
            adv_obj.author = request.user
            adv_obj.save()
            
    form = Advmodelform()
    context = {'form': form}

    return render(request,"advertisement-post.html",context=context)

def registr(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")

def profile(request):
    return render(request,"profile.html")