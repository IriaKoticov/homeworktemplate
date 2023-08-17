from django.db import models

# Create your models here.


class Advertisement(models.Model): #это класс модель
    id = models.AutoField(primary_key=True)
    title = models.CharField("заголовок",max_length=64)
    text = models.TextField("описание")
    author = models.CharField("автор",max_length=64)
    date = models.DateField("дата", auto_now_add=True)

    def __repr__(self):
        return f"<Advertisement: Advertisement(id={self.id}, title={self.title}, text={self.text}, author={self.author})>"
    
    class Meta:
        db_table = 'advertisements'
        managed = True
        verbose_name = 'advertisements'
        verbose_name_plural = 'advertisements'

    