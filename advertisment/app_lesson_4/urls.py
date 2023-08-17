from django.urls import path
from .views import index,top_sellers,post_ads,registr,login,profile,debug

urlpatterns = [path("",index,name="main"),path("top-sellers",top_sellers,name="tp"),
               path("advertisement-post",post_ads,name="adv"),path("register",registr,name="rg"),
               path("login",login,name="log"),path("profile",profile,name="pf"),path("debug",debug)]