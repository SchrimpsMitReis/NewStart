from django.contrib import admin
from .models import Product, Producttype, Bill, Order, Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_filter = ['first_name', 'last_name']
    list_display = ['last_name', 'first_name', 'email_address']

    readonly_fields = ['account']

    # prepopulated_fields = {
    #     "slug" : ['first_name', 'last_name']
    # }

    fieldsets = [
        (
            None,
            {
                "fields": ["first_name", "last_name", "account"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["newsletter_abo",], # 'slug'
            },
        ),
    ]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


admin.site.register(Product, ProductAdmin)
admin.site.register(Producttype)
admin.site.register(Bill)
admin.site.register(Order)
admin.site.register(Customer, CustomerAdmin)