from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^stocks/$', views.StockListView.as_view(), name='stocks'),
	url(r'^stock/(?P<pk>[0-9]+)$', views.StockDetailView.as_view(), name='stock-detail'),
]