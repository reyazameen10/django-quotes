# mini_insta/admin.py

from django.contrib import admin
from .models import Profile

# Register your models here.
admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'display_name', 'profile_image', 'profile_image_url', 'bio_text', 'join_date', 'image_url')