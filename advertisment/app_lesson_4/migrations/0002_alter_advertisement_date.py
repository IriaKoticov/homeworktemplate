# Generated by Django 4.2.3 on 2023-08-17 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lesson_4', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='дата'),
        ),
    ]
