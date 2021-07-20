# Generated by Django 3.2.4 on 2021-07-20 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MotoSell', '0052_alter_pojazdy_rodzaj_paliwa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pojazdy',
            name='Kategoria',
            field=models.CharField(choices=[('Osobowy', 'Osobowy'), ('Ciezarowy', 'Ciezarowy'), ('Motocykl', 'Motocykl')], default='', max_length=24),
        ),
        migrations.AlterField(
            model_name='pojazdy',
            name='Rodzaj_paliwa',
            field=models.CharField(choices=[('LPG', 'LPG'), ('Benzyna', 'Benzyna'), ('Diesel', 'Diesel')], default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='pojazdy',
            name='Uzytkownik',
            field=models.CharField(max_length=64),
        ),
    ]
