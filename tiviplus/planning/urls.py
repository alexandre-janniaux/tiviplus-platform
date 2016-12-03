from django.conf.urls import url

from planning.views import (
	MaterialLoanListView,
	MaterialLoanCreateView,
	MaterialLoanUpdateView,
	MaterialLoanDeleteView,
)


app_name = "planning"

urlpatterns = [
	url(r'create/$', MaterialLoanCreateView.as_view(), name='create-loan'),
	url(r'update/(?P<pk>[0-9]+)/$', MaterialLoanUpdateView.as_view(), name='update-loan'),
	url(r'delete/(?P<pk>[0-9]+)/$', MaterialLoanDeleteView.as_view(), name='delete-loan'),
	url(r'', MaterialLoanListView.as_view(), name='list-loan'),
]
