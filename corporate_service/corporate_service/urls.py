from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from secret_santa.views import (ProfileViewSet, SantaCaseViewSet,
                                WishViewSet, SantaMatchViewSet,
                                WishStatusViewSet)

santa_router = routers.DefaultRouter()
santa_router.register('profile', ProfileViewSet)
santa_router.register('santa_case', SantaCaseViewSet)
santa_router.register('wish', WishViewSet)
santa_router.register('santa_match', SantaMatchViewSet)
santa_router.register('wish_sttaus', WishStatusViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(santa_router.urls))
]
