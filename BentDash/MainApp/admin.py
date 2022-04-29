from django.contrib import admin
from .models import Category, Banner, Product, AboutUs, Contact, ContactUs, Stars, ProductBanner




admin.site.register(Category)
admin.site.register(Banner)
admin.site.register(Product)
admin.site.register(ProductBanner)
admin.site.register(AboutUs)
admin.site.register(Contact)
admin.site.register(ContactUs)
admin.site.register(Stars)