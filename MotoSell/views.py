from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import PojazdySerializer, PojazdyMiniSerializer,UserSerializer
from MotoSell.models import Pojazdy
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import filters
# Create your views here.
# User auth viewsets
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)


class RegisterUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

##Content
class PojazdyViewset(viewsets.ModelViewSet):
    serializer_class = PojazdySerializer
    queryset = Pojazdy.objects.all()

