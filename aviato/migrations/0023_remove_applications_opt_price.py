# Generated by Django 4.0.5 on 2022-08-10 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aviato', '0022_applications_opt_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applications',
            name='opt_price',
        ),
    ]