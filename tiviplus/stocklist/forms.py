from django import forms

from .models import MaterialDefCategory

class MaterialDefCreateForm(forms.Form):
	photo = forms.ImageField(required=False)
	name  = forms.CharField(max_length=100)
	category = forms.ChoiceField(choices=MaterialDefCategory.objects.all())
	acquisition_date = forms.DateTimeField()
	price = forms.IntegerField()
	comments = forms.CharField(widget=forms.Textarea)


