from django.contrib import admin
from .models import Market
# Register your models here.
class MarketAdmin(admin.ModelAdmin):
  list_display = ("timestamp", "transactionhash", "address",)

admin.site.register(Market, MarketAdmin)