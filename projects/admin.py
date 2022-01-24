from django.contrib import admin

from .models import Pokemon, Type, Color

admin.site.register(Pokemon)
admin.site.register(Type)
admin.site.register(Color)