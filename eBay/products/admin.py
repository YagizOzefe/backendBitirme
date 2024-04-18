from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','slug','created_at']
    readonly_fields = ['id', 'slug', 'created_at']


admin.site.register(Kategori)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sepet)

