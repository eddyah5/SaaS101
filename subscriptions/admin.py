from django.contrib import admin

# Register your models here.

from subscriptions.models import StripeCustomer


admin.site.register(StripeCustomer)