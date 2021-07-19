from rest_framework import serializers
from .models import Pojazdy
from django.contrib.auth.models import User

class PojazdySerializer(serializers.ModelSerializer):

    class Meta:
        model = Pojazdy
        fields = ['id', 'Tytul', 'Kategoria', 'Marka', 'Model', 'Opis',
                  'Rodzaj_paliwa', 'Rok_produkcji', 'Przebieg',
                  'Pojemnosc_skokowa', 'Moc', 'Data_dodania', 'Data_publikacji', 'Zdjecie','Uzytkownik']



class PojazdyMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pojazdy
        fields = ['id', 'Tytul', 'Opis']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password' : {'write_only' : True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

