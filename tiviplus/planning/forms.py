from django import forms
from stocklist.models import MaterialDef
from django.utils.translation import ugettext as _

class LoanMultipleChoiceField(forms.ModelMultipleChoiceField):

	def label_from_instance(self, obj):
		return obj.name


class MaterialLoanCreateForm(forms.Form):
	date     = forms.DateTimeField()
	end_date = forms.DateTimeField()
	reason   = forms.CharField()

	loans    = LoanMultipleChoiceField(queryset=MaterialDef.objects.all())
