from rest_framework import serializers
from .models import Profile, Wish, WishStatus, SantaMatch


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = '__all__'


class WishStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishStatus
        fields = '__all__'


class SantaMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SantaMatch
        fields = '__all__'
