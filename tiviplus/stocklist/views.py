from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import MaterialDef, MaterialDefCategory
from .forms import MaterialDefCreateForm

class StocklistListView(ListView):
	queryset = MaterialDef.objects.all().order_by('category').order_by('name')
	context_object_name = 'stocklist_list'

	def get_context_data(self, **kwargs):
		context = super(StocklistListView, self).get_context_data(**kwargs)
		context['material_create_form'] = MaterialDefCreateForm()
		return context


class StocklistDetailView(DetailView):
	model = MaterialDef

class StocklistCreateView(CreateView):
	model = MaterialDef

class StocklistUpdateView(UpdateView):
	model = MaterialDef

class StocklistDeleteView(DeleteView):
	model = MaterialDef
