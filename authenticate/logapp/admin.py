from django.contrib import admin

# Register your models here.
from . models import student
from .models import emp
class StudentAdmin(admin.ModelAdmin):
    list_display= ['rollnum','name','add']
admin.site.register(student,StudentAdmin)
class EmpAdmin(admin.ModelAdmin):
    list_display = ['eid','ename','eadd']
admin.site.register(emp,EmpAdmin)