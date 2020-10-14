from django.contrib import sitemaps
from django.urls import reverse


# Sitemap
class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return ['index', 'about', 'contact', 'services']

    def location(self, item):
        return reverse(item)
