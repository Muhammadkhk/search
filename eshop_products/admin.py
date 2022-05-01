from django.contrib import admin

# Register your models here.

from .models import Product,Product1,Product2


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'active']
    list_editable = []

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)

class ProductAdmin1(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'active']
    list_editable = []

    class Meta:
        model = Product1


admin.site.register(Product1, ProductAdmin1)

class ProductAdmin2(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'active']
    list_editable = []

    class Meta:
        model = Product2


admin.site.register(Product2, ProductAdmin)