from django import forms

class MaterialLoanCreateForm(forms.Form):
	number   = forms.IntegerField()
	date     = forms.DateTimeField()
	end_date = forms.DateTimeField()
	reason   = forms.CharField()

