from django.db import models
from django.contrib import admin
from django.utils import timezone,html
# Create your models here.


class Advertisement(models.Model): #это класс модель
    id = models.AutoField(primary_key=True)
    title = models.CharField("заголовок",max_length=64)
    text = models.TextField("описание")
    author = models.CharField("автор",max_length=64)
    date = models.DateField("дата", auto_now_add=True)
    updated_at = models.DateTimeField("обновление",auto_now=True)
    prise = models.FloatField("цена")
    auction = models.BooleanField("торг",default=False)
    
    


    @admin.display(description="Когда создано")
    def hende_date(self):
        if self.date == timezone.now().date():
            return html.format_html('<span style="color: green; font-weight:bold;">Сегодня</span>')
        return self.date.strftime("%d.%m.%Y") 
    
    @admin.display(description="Обновление")
    def updatetime(self):
        if self.updated_at.strftime("%d.%m.%Y") == timezone.now().date().strftime("%d.%m.%Y"):
            return html.format_html('<span style="color: red; font-weight:bold;">Сегодня</span>')
        return self.updated_at.strftime("%d.%m.%Y")

    def __repr__(self):
        return f"<Advertisement: Advertisement(id={self.id}, title={self.title}, text={self.text}, author={self.author})>"
    


    class Meta:
        db_table = 'advertisements'
        managed = True
        verbose_name = 'advertisements'
        verbose_name_plural = 'advertisements'

    