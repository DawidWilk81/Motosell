# Generated by Django 3.2.4 on 2021-07-08 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MotoSell', '0027_auto_20210707_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pojazdy',
            name='Uzytkownik',
        ),
        migrations.AlterField(
            model_name='pojazdy',
            name='Data_dodania',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='pojazdy',
            name='Kategoria',
            field=models.CharField(choices=[('Osobowy', 'Osobowy'), ('Ciezarowy', 'Ciezarowy'), ('Motocykl', 'Motocykl')], default='', max_length=24),
        ),
        migrations.AlterField(
            model_name='pojazdy',
            name='Rodzaj_paliwa',
            field=models.CharField(choices=[('Diesel', 'Diesel'), ('LPG', 'LPG'), ('Benzyna', 'Benzyna')], default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='pojazdy',
            name='Zdjecie',
            field=models.ImageField(null=True, upload_to='zdjecia_samochodow'),
        ),
        migrations.AlterField(
            model_name='pojazdytest',
            name='Kategoria',
            field=models.CharField(choices=[('Osobowy', 'Osobowy'), ('Ciezarowy', 'Ciezarowy'), ('Motocykl', 'Motocykl')], default='', max_length=24),
        ),
        migrations.AlterField(
            model_name='pojazdytest',
            name='Rodzaj_paliwa',
            field=models.CharField(choices=[('Diesel', 'Diesel'), ('LPG', 'LPG'), ('Benzyna', 'Benzyna')], default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='pojazdytest',
            name='Zdjecie',
            field=models.ImageField(null=True, upload_to='zdjecia_samochodow'),
        ),
    ]
