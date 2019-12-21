from django.contrib import admin

# Register your models here.
from .models import student


class studentAdmin(admin.ModelAdmin):
    list_display = ['sid','sname','sadd','sph']

admin.site.register(student,studentAdmin)