from django.contrib import admin
from .models import Diary
# Register your models here.

admin.site.register(Diary)



class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title','publish')