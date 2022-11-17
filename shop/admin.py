from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Gender)
admin.site.register(Brend)
admin.site.register(Category)
admin.site.register(Subb_category)
admin.site.register(Size)
admin.site.register(Commentler)
admin.site.register(Color)
admin.site.register(Favori)
admin.site.register(AddImage)

class ProductIMage(admin.StackedInline):
    model = AddImage
    max_num=5
    extra=1

class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductIMage]

admin.site.register(Clothes, ProductAdmin)