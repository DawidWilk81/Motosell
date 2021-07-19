# Generated by Django 3.2.4 on 2021-07-05 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MotoSell', '0019_auto_20210704_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pojazdy',
            name='Data_publikacji',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='pojazdy',
            name='Kategoria',
            field=models.CharField(choices=[('Ciezarowy', 'Ciezarowy'), ('Osobowy', 'Osobowy'), ('Motocykl', 'Motocykl')], max_length=24),
        ),
        migrations.AlterField(
            model_name='pojazdy',
            name='Rodzaj_paliwa',
            field=models.CharField(choices=[('Diesel', 'Diesel'), ('Benzyna', 'Benzyna'), ('LPG', 'LPG')], max_length=64),
        ),
    ]
