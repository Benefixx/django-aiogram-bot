# Generated by Django 4.1.1 on 2022-10-15 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviato', '0026_alter_applications_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='create_time',
            field=models.DateField(auto_now_add=True, verbose_name='Время создания'),
        ),
    ]