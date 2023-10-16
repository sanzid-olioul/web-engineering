from django.contrib import admin
from .models import Singer

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['singer_name','singer_bio','date_of_birth']
