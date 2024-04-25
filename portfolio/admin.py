from django.contrib import admin
from .models import Profile, Photo, Comment


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'age', 'rating']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['profile', 'image', 'tags', 'nudity_checked']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['photo', 'user', 'text', 'created_at']
