from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView, 
	DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import MaterialLoan
from .forms  import MaterialLoanCreateForm

class MaterialLoanListView(ListView):
	queryset = MaterialLoan.objects.all().order_by('borrower').order_by('-date').filter(returned_date__isnull=True)
	context_object_name = 'material_loans'

	def get_context_data(self, **kwargs):
		context = super(MaterialLoanListView, self).get_context_data(**kwargs)
		context['loan_form'] = MaterialLoanCreateForm()
		return context


class MaterialLoanDetailView(DetailView):
	model = MaterialLoan

class MaterialLoanCreateView(CreateView, LoginRequiredMixin):
	model = MaterialLoan
	form_class = MaterialLoanCreateForm

	def form_valid(self, form):
		if not form.instance.borrower:
			form.instance.borrower = self.user

class MaterialLoanUpdateView(UpdateView, LoginRequiredMixin):
	model = MaterialLoan

class MaterialLoanDeleteView(DeleteView, LoginRequiredMixin):
	model = MaterialLoan
