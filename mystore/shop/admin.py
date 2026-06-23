from django.contrib import admin

from .models import Product
from .category import Category
from .models import Customer


# CATEGORY ADMIN
class CategoryAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'name'
    ]


# PRODUCT ADMIN
class ProductAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'name',
        'category',
        'price',
        'old_price',
        'rating'
    ]

    list_filter = [
        'category'
    ]

    search_fields = [
        'name'
    ]


# CUSTOMER ADMIN
class CustomerAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
        'mobile'
    ]

    search_fields = [
        'first_name',
        'last_name',
        'email'
    ]


# REGISTER MODELS
admin.site.register(Product, ProductAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Customer, CustomerAdmin)