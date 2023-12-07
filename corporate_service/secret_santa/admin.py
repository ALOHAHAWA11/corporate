from django.contrib import admin
from .models import Profile, Wish, WishStatus, SantaMatch

admin.site.register(Profile)
admin.site.register(Wish)
admin.site.register(WishStatus)
admin.site.register(SantaMatch)
