from rest_framework import viewsets
from .models import Profile, Wish, WishStatus, SantaMatch, SantaCase
from .serailizers import (ProfileSerializer, WishSerializer,
                          WishStatusSerializer, SantaMatchSerializer,
                          SantaCaseSerializer)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class WishViewSet(viewsets.ModelViewSet):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer


class WishStatusViewSet(viewsets.ModelViewSet):
    queryset = WishStatus.objects.all()
    serializer_class = WishStatusSerializer


class SantaMatchViewSet(viewsets.ModelViewSet):
    queryset = SantaMatch.objects.all()
    serializer_class = SantaMatchSerializer


class SantaCaseViewSet(viewsets.ModelViewSet):
    queryset = SantaCase.objects.all()
    serializer_class = SantaCaseSerializer
