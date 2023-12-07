from django.contrib import admin
from django.urls import path
from secret_santa.views import (ProfileAPIView, WishAPIView, 
                                WishStatusAPIView, SantaMatchAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/profile', ProfileAPIView.as_view()),
    path('api/v1/wish', WishAPIView.as_view()),
    path('api/v1/wish_status', WishStatusAPIView.as_view()),
    path('api/v1/santa_match', SantaMatchAPIView.as_view())
]
