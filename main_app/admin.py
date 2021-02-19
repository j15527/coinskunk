from django.contrib import admin
from . models import Asset, Portfolio
# Register your models here.

admin.site.register(Portfolio)
admin.site.register(Asset)
