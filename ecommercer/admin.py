from django.contrib import admin
from .models import userinfo,abouts
from .models import product

# Register your models here.
admin.site.register(userinfo)
admin.site.register(product)
admin.site.register(abouts)

