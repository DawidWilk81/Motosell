# Generated by Django 3.2.4 on 2021-07-03 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MotoSell', '0010_auto_20210702_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pojazdy',
            name='Kategoria',
            field=models.CharField(choices=[('A', 'Osobowy'), ('N', 'Ciezarowy'), ('N', 'Motocykl')], max_length=24),
        ),
        migrations.AlterField(
            model_name='pojazdy',
            name='Rodzaj_paliwa',
            field=models.CharField(choices=[('V', 'Benzyna'), ('A', 'Diesel'), ('R', 'LPG')], max_length=64),
        ),
    ]
