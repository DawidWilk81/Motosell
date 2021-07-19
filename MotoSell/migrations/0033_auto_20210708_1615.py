# Generated by Django 3.2.4 on 2021-07-08 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MotoSell', '0032_auto_20210708_1614'),
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
            field=models.CharField(choices=[('LPG', 'LPG'), ('Benzyna', 'Benzyna'), ('Diesel', 'Diesel')], default='', max_length=64),
        ),
    ]
