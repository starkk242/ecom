from django.contrib import admin
from .models import Product, Category, Images


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'featured', )
    list_filter = ('name', 'price', 'quantity', 'featured', )
    list_editable = ('price', 'quantity', )

    # sets up slug to be generated from product name
    prepopulated_fields = {'slug': ('name', )}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )

class ImagesAdmin(admin.ModelAdmin):
    list_display = ('images','product_id', )
    list_display_links = ('images','product_id',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Images, ImagesAdmin)