from django.contrib import admin
from planning.models import MaterialLoan, Event

class MaterialLoanAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
	pass

admin.site.register(MaterialLoan)
admin.site.register(Event)


