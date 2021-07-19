from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

class Pojazdy(models.Model):

    Benzyna='Benzyna'
    Diesel='Diesel'
    LPG='LPG'

    Motocykl = 'Motocykl'
    Osobowy='Osobowy'
    Ciezarowy='Ciezarowy'

    Rodzaj_paliwa = {
        (Benzyna, 'Benzyna'),
        (Diesel, 'Diesel'),
        (LPG, 'LPG'),
    }
    Typ_pojazdu = {
        (Motocykl, 'Motocykl'),
        (Osobowy, 'Osobowy'),
        (Ciezarowy, 'Ciezarowy'),
    }
    Tytul = models.CharField(max_length=128)
    Kategoria = models.CharField(max_length=24, choices=Typ_pojazdu, default='')
    Opis = models.TextField(default='')
    Marka = models.CharField(max_length=64, default='')
    Model = models.CharField(max_length=64, default='')
    Rodzaj_paliwa = models.CharField(choices=Rodzaj_paliwa, max_length=64, default='')
    Rok_produkcji = models.IntegerField(default=0)
    Przebieg = models.IntegerField(default=0)
    Pojemnosc_skokowa = models.IntegerField(default=0)
    Moc = models.IntegerField(default=0)
    Uzytkownik = models.CharField( max_length=64, null=False)
    Zdjecie = models.ImageField(upload_to='zdjecia_samochodow', null=True)
    Data_dodania = models.DateField(null=True, auto_now=True)
    Data_publikacji = models.DateField(null=True, auto_now=True)
    def __str__(self):
        return self.Tytul



