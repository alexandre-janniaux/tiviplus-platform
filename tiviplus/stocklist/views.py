from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import MaterialDef, MaterialDefCategory
from .forms import MaterialDefCreateForm, CategoryCreateForm

class StocklistListView(ListView):
	queryset = MaterialDef.objects.all().order_by('category').order_by('name')
	context_object_name = 'stocklist_list'

	def get_context_data(self, **kwargs):
		context = super(StocklistListView, self).get_context_data(**kwargs)
		context['material_create_form'] = MaterialDefCreateForm()
		context['category_create_form'] = CategoryCreateForm()
		return context


class StocklistDetailView(DetailView):
	model = MaterialDef

class StocklistCreateView(CreateView):
	model = MaterialDef
	form_class = MaterialDefCreateForm
	success_url = reverse_lazy('stocklist:list-material')

class StocklistUpdateView(UpdateView):
	model = MaterialDef

class StocklistDeleteView(DeleteView):
	model = MaterialDef

class StocklistCategoryCreateView(CreateView):
	model = MaterialDefCategory
	fields = ['name']
	success_url = reverse_lazy('stocklist:list-material')
