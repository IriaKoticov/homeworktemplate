from django.db import models
from django.contrib import admin
from django.utils import timezone,html
from django.contrib.auth import get_user_model
import django.forms as fm
from django.forms import ModelForm
# Create your models here.


    
def examination(value):
    if value[0] == "?":
        raise ValueError("Заголовок не может начинаться с вопросительного знака и форма не проходила валидацию.")


User = get_user_model()

class Advertisement(models.Model): #это класс модель
    id = models.AutoField(primary_key=True)
    title = models.CharField("заголовок",max_length=64,validators=[examination])
    text = models.TextField("описание")
    author = models.ForeignKey(to=User,on_delete=models.CASCADE)
    date = models.DateField("дата", auto_now_add=True)
    updated_at = models.DateTimeField("обновление",auto_now=True)
    prise = models.FloatField("цена")
    auction = models.BooleanField("торг",default=False)
    coortun = models.ImageField("изображения",upload_to="media",default="static/img/adv.png")


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
    
    @admin.display(description="Картинка")
    def imgpre(self):
        return html.format_html(f'<img src="{ self.coortun.url}" height="100" width="100">')

    def __repr__(self):
        return f"<Advertisement: Advertisement(id={self.id}, title={self.title}, text={self.text}, author={self.author})>"
    


    class Meta:
        db_table = 'advertisements'
        managed = True
        verbose_name = 'advertisements'
        verbose_name_plural = 'advertisements'


class Advmodelform(ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title','text','prise','auction','coortun']
        widgets = {
                    'title': fm.TextInput(attrs={"class":"form-control form-control-lg"}),
                    'text':fm.Textarea(attrs={"class":"form-control form-control-lg"}),
                    'prise':fm.NumberInput(attrs={"class":"form-control form-control-lg"}),
                    'auction':fm.CheckboxInput(attrs={"class":"form-check-input"})
                    }