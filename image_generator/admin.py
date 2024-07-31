from django.contrib import admin
from .models import GeneratedImage, TestUser

# Register your models here.

admin.site.register(GeneratedImage)
admin.site.register(TestUser)