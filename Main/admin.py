from django.contrib import admin
from .models import Client, Testimonial, Team, Service, Blog, WebsiteDetail

# Register your models here.

admin.site.register(Client)
admin.site.register(Testimonial)
admin.site.register(Team)
admin.site.register(Service)
admin.site.register(Blog)
admin.site.register(WebsiteDetail)