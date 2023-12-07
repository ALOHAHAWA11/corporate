from rest_framework import generics
from .models import Profile, Wish, WishStatus, SantaMatch
from .serailizers import (ProfileSerializer, WishSerializer,
                          WishStatusSerializer, SantaMatchSerializer)


class ProfileAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class WishAPIView(generics.ListAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer


class WishStatusAPIView(generics.ListAPIView):
    queryset = WishStatus.objects.all()
    serializer_class = WishStatusSerializer


class SantaMatchAPIView(generics.ListAPIView):
    queryset = SantaMatch.objects.all()
    serializer_class = SantaMatchSerializer
