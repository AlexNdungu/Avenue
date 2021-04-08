from django.contrib.sitemaps import Sitemap
from .models import Movies
from django.urls import reverse

class MoviesSitemap(Sitemap):
    def items(self):
        return Movies.objects.all()

class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['avenueShop:index',]

    def location(self, item):
            return reverse(item)        