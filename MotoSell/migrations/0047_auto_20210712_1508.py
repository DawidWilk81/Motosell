# Generated by Django 3.2.4 on 2021-07-12 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MotoSell', '0046_auto_20210712_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pojazdy',
            name='Kategoria',
            field=models.CharField(choices=[('Motocykl', 'Motocykl'), ('Ciezarowy', 'Ciezarowy'), ('Osobowy', 'Osobowy')], default='', max_length=24),
        ),
        migrations.AlterField(
            model_name='pojazdy',
            name='Rodzaj_paliwa',
            field=models.CharField(choices=[('Benzyna', 'Benzyna'), ('Diesel', 'Diesel'), ('LPG', 'LPG')], default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='pojazdy',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
