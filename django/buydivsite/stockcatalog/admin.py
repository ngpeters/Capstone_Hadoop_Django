# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Company, ProfitUse, Stock

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'ticker_symbol', 'date_of_IPO')

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('stockname', 'company', 'display_profituse')

#admin.site.register(Company)
admin.site.register(Company, CompanyAdmin)

#admin.site.register(Stock)

admin.site.register(ProfitUse)
