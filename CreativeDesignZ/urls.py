"""CreativeDesignZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from froala_editor import views
from django.contrib.sitemaps.views import sitemap
from Main.sitemaps import StaticViewSitemap, BlogSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'book' : BlogSitemap
}

urlpatterns = [
    path('', include('Main.urls')),
    path('sitemap.xml', sitemap, {'sitemaps' : sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('robots.urls')),
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('froala_editor/',include('froala_editor.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'Main.views.error_404_view'
handler500 = 'Main.views.error_500_view'