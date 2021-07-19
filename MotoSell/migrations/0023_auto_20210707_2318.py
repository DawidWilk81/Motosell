# Generated by Django 3.2.4 on 2021-07-07 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MotoSell', '0022_auto_20210707_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pojazdy',
            name='Marka',
        ),
        migrations.RemoveField(
            model_name='pojazdy',
            name='Model',
        ),
        migrations.RemoveField(
            model_name='pojazdy',
            name='Opis',
        ),
        migrations.AddField(
            model_name='pojazdytest',
            name='Marka',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='pojazdytest',
            name='Model',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='pojazdytest',
            name='Opis',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='pojazdy',
            name='Rodzaj_paliwa',
            field=models.CharField(choices=[('Diesel', 'Diesel'), ('Benzyna', 'Benzyna'), ('LPG', 'LPG')], max_length=64),
        ),
        migrations.AlterField(
            model_name='pojazdytest',
            name='Kategoria',
            field=models.CharField(choices=[('Ciezarowy', 'Ciezarowy'), ('Motocykl', 'Motocykl'), ('Osobowy', 'Osobowy')], default='', max_length=24),
        ),
    ]
