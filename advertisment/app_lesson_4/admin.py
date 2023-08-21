from django.contrib import admin
from .models import Advertisement


class AdvAdmin(admin.ModelAdmin):
    list_display =['id','title','date','auction',"hende_date","updatetime"]
    list_filter =["title","date"]
    actions=["deldescr","mkaucttrue"]

    fieldsets = (
                ("Общее",{"fields":("title","text")}),
                ("финансы",{"fields":("auction","prise"),"classes":["collapse"]})
                )

    @admin.action(description="Удалить описание объектов")
    def deldescr(self,request,queryset):
        queryset.update(text='')

    @admin.action(description="Включить возможность торга")
    def mkaucttrue(self,request,queryset):
        queryset.update(auction=True)
    


# Register your models here.
admin.site.register(Advertisement,AdvAdmin)