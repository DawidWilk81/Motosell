# Generated by Django 3.2.4 on 2021-06-26 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pojazdy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tytul', models.CharField(max_length=128)),
                ('Opis', models.TextField(default='')),
                ('Kategoria', models.CharField(choices=[('A', 'Osobowy'), ('N', 'Motocykl'), ('N', 'Ciezarowy')], max_length=24)),
                ('Marka', models.CharField(max_length=64)),
                ('Model', models.CharField(max_length=64)),
                ('Rok_produkcji', models.IntegerField(default=0)),
                ('Przebieg', models.IntegerField(default=0)),
                ('Pojemnosc_skokowa', models.IntegerField(default=0)),
                ('Moc', models.IntegerField(default=0)),
                ('Rodzaj_paliwa', models.CharField(choices=[('R', 'LPG'), ('A', 'Diesel'), ('V', 'Benzyna')], max_length=64)),
                ('Zdjecie', models.ImageField(upload_to='zdjecia_samochodow')),
                ('Data_publikacji', models.DateField(null=True)),
                ('Uzytkownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
