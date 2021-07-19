from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

from . import views
from MotoSell.views import PojazdyViewset, UserViewSet, RegisterUserViewSet

from django.conf.urls.static import  static
from django.conf import settings

router = routers.DefaultRouter()
router.register('pojazdy', PojazdyViewset)
router.register('pojazdy/:id', PojazdyViewset)
router.register('users', RegisterUserViewSet)



urlpatterns = [
    path('auth/', ObtainAuthToken.as_view()),
    path('', include(router.urls)),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
