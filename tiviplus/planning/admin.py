from django.contrib import admin
from planning.models import MaterialLoan

class MaterialLoanAdmin(admin.ModelAdmin):
    pass

admin.site.register(MaterialLoan)


