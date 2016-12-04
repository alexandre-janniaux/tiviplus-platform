from django import forms

from .models import MaterialDef, MaterialDefCategory

class MaterialDefCreateForm(forms.ModelForm):
	class Meta:
		model = MaterialDef
		fields = ['photo', 'name', 'category', 'acquisition_date', 'price', 'comments']


class CategoryCreateForm(forms.ModelForm):
	class Meta:
		model = MaterialDefCategory
		fields = ['name']
