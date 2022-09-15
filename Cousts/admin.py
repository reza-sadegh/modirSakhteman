from django.contrib import admin
from .models import Categories,Cousts

class CoustsAdmin(admin.ModelAdmin):
    list_display = ('Description','Amount','payTime','category_name','Recipient','AccountNumber','invoice','tel')

admin.site.register(Cousts,CoustsAdmin)

class CategoriessAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

admin.site.register(Categories,CategoriessAdmin)
# Register your models here.
