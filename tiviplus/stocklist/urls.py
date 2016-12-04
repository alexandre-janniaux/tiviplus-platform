from django.conf.urls import url

from .views import (
	StocklistListView,
	StocklistCreateView,
	StocklistUpdateView,
	StocklistDeleteView,
	StocklistCategoryCreateView,
)


app_name = "stocklist"

urlpatterns = [
	url(r'category/create/$',       StocklistCategoryCreateView.as_view(), name='create-category'),
	url(r'create/$',                StocklistCreateView.as_view(), name='create-material'),
	url(r'update/(?P<pk>[0-9]+)/$', StocklistUpdateView.as_view(), name='update-material'),
	url(r'delete/(?P<pk>[0-9]+)/$', StocklistDeleteView.as_view(), name='delete-material'),
	url(r'',                        StocklistListView.as_view(),   name='list-material'),
]
