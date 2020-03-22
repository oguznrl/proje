from django.contrib import admin
from .models import Product,Company
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "count", "company_name","price")
    search_fields = ["name", "company_name"]
    list_filter = ["company_name"]

    class Meta:
        model = Product


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]

    class Meta:
        model = Company

