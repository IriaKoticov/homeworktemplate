# Generated by Django 4.2.3 on 2023-08-17 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lesson_4', '0005_alter_advertisement_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
