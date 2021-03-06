# Generated by Django 3.2.4 on 2021-07-08 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MotoSell', '0028_auto_20210708_1513'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PojazdyTest',
        ),
        migrations.AddField(
            model_name='pojazdy',
            name='Uzytkownik',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pojazdy',
            name='Kategoria',
            field=models.CharField(choices=[('Osobowy', 'Osobowy'), ('Motocykl', 'Motocykl'), ('Ciezarowy', 'Ciezarowy')], default='', max_length=24),
        ),
        migrations.AlterField(
            model_name='pojazdy',
            name='Rodzaj_paliwa',
            field=models.CharField(choices=[('LPG', 'LPG'), ('Benzyna', 'Benzyna'), ('Diesel', 'Diesel')], default='', max_length=64),
        ),
    ]
