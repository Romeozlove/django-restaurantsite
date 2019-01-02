from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)
# Register your models here.

admin.site.register(Menu, MenuAdmin)