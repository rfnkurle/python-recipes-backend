from django.contrib import admin

from .models import Recipe

models_list = [Recipe]
admin.site.register(models_list)
