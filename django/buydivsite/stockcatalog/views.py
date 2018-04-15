# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic

from .models import Company, ProfitUse, Stock

# Create your views here.

def index(request):
	"""
	View function for home page of site.
	"""
	# Generate counts of some of the main objects
	num_stocks=Stock.objects.all().count()
	num_companies=Company.objects.count()  # The 'all()' is implied by default.
	
	# Render the HTML template index.html with the data in the context variable
	return render(
		request,
		'index.html',
		context={'num_stocks':num_stocks,'num_companies':num_companies},
	)

class StockListView(generic.ListView):
	model = Stock
	paginate_by = 10

class StockDetailView(generic.DetailView):
    model = Stock