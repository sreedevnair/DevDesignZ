from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from django.utils.text import slugify
from .models import Blog

class StaticViewSitemap(Sitemap):

    changefreq = 'daily'


    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):

    changefreq = "daily"

    def items(self):
        return Blog.objects.all()

    def location(self, obj):
        return '/blog/%s' % (slugify(obj))
