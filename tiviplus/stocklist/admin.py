from django.contrib import admin
from stocklist.models import MaterialDef, MaterialDefCategory

class MaterialDefAdmin(admin.ModelAdmin):
    pass

class MaterialDefCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(MaterialDef)
admin.site.register(MaterialDefCategory)

# Register your models here.
