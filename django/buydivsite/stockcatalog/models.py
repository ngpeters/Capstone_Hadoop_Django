# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class ProfitUse(models.Model):
	"""
	Model representing type of profit use (e.g. buyback or dividends).
	"""
	name = models.CharField(max_length=200, help_text="Enter a profit use (e.g. Buyback or Dividen)")
	
	def __str__(self):
		"""
		String for representing the Model object (in Admin site etc.)
		"""
		return self.name

@python_2_unicode_compatible
class Stock(models.Model):
	"""
	Model representing a stock (but not a specific copy of a stock).
	"""
	stockname = models.CharField(max_length=200)
	company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
	# Foreign Key used because stock can only have one company, but company can have different classes of stock
	# usually denoted as class A or class B. They would then also have different dividen payouts.
	# Company as a string rather than object because it hasn't been declared yet in the file.
	summary = models.TextField(max_length=1000, help_text='Enter a brief description of the stock')
	tickersymbol = models.CharField('TickerSymbol',max_length=5, help_text='Ticker symbole used to identify publicly traded shares')
	profituse = models.ManyToManyField(ProfitUse, help_text='Select a profituse for this stock')
	# ManyToManyField used because profituse can contain many stocks. stocks can cover many profituses, 
	# in this app they will not but it could be if there were more than two being tested.
	# ProfitUse class has already been defined so we can specify the object above.
	
	def __str__(self):
		"""
		String for representing the Model object.
		"""
		return self.stockname
	
	
	def get_absolute_url(self):
		"""
		Returns the url to access a detail record for this stock.
		"""
		return reverse('stock-detail', args=[str(self.id)])

	def display_profituse(self):
		"""
		Creates a string for the Profit Use. This is required to display profituse in Admin.
		"""
		return ', '.join([ profituse.name for profituse in self.profituse.all()[:3] ])
	display_profituse.short_description = 'ProfitUse'


@python_2_unicode_compatible
class Company(models.Model):
	"""
	Model representing an company.
	"""
	company_name = models.CharField(max_length=100)
	ticker_symbol = models.CharField(max_length=5)
	date_of_IPO = models.DateField(null=True, blank=True)

	class Meta:
		ordering = ["ticker_symbol","company_name"]
	
	def get_absolute_url(self):
		"""
		Returns the url to access a particular company instance.
		"""
		return reverse('company-detail', args=[str(self.id)])
	

	def __str__(self):
		"""
		String for representing the Model object.
		"""
		return '{0}, {1}'.format(self.ticker_symbol,self.company_name)

		