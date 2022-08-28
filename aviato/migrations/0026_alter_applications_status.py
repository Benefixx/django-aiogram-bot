# Generated by Django 4.0.6 on 2022-08-28 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviato', '0025_alter_applications_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='status',
            field=models.CharField(blank=True, choices=[('Подтвержден', 'Подтвержден'), ('Отменен', 'Отменен'), ('Передан упаковщику', 'Передан упаковщику'), ('Передан логисту', 'Передан логисту'), ('Упакован', 'Упакован'), ('Доставлен', 'Доставлен'), ('Фабричный брак', 'Фабричный брак'), ('Дорожный брак', 'Дорожный брак'), ('Ожидание подтверждения', 'Ожидание подтверждения'), ('В дороге', 'В дороге')], default='Ожидание подтверждения', max_length=200, null=True, verbose_name='Статус'),
        ),
    ]
