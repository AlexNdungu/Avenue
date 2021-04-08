from django.contrib.sitemaps import Sitemap
from .models import Movies
from django.urls import reverse

class MoviesSitemap(Sitemap):
    def items(self):
        return Movies.objects.all()