from django.contrib.sitemaps import Sitemap
from .models import Movies

class MoviesSitemap(Sitemap):
    def items(self):
        return Movies.objects.all()