from django.contrib.sitemaps import Sitemap
from .models import Customer
from django.urls import reverse

class CustomerSitemap(Sitemap):
    def itemc(self):
        return Customer.objects.all()