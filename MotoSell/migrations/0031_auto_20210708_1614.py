# Generated by Django 3.2.4 on 2021-07-08 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MotoSell', '0030_auto_20210708_1609'),
    ]

    operations = [
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
