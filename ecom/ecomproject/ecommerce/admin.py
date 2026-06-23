from django.contrib import admin
from.models import *


class Pro_codes(admin.ModelAdmin):
    list_display=('name','code')
    
admin.site.register(ProductCode,Pro_codes)

class Products(admin.ModelAdmin):
    list_display=('product_name','product_code','quantity')

admin.site.register(AllProducts,Products)

admin.site.register(Profile)
admin.site.register(CartItem)