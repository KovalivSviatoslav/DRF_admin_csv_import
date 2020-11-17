from django.contrib import admin
from django.urls import path

from .views import import_csv
from .models import Customer, Order


# Register your models here.
@admin.register(Customer)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'date_of_birth', 'created_at', 'order')
    fields = (('first_name', 'last_name'), 'date_of_birth', 'order', 'created_at')
    change_list_template = 'import_csv.html'

    def get_urls(self):
        urls = super(CustomersAdmin, self).get_urls()
        my_urls = [
            path('import-csv/', import_csv),
        ]

        return my_urls + urls


@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'created_at', 'customer')
    fields = ('product_name', 'created_at')
