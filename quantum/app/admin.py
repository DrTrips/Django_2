from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Article)
admin.site.register(Comment)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
   list_display = ['id', 'user_surname', 'user_name', 'user_age']