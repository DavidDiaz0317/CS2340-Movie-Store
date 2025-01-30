from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
    ordering = ['name']
# Register your models here.
