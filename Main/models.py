from django.db import models
from froala_editor.fields import FroalaField
from .helpers import *

# Create your models here.

class Client(models.Model):
    Company = models.CharField(max_length=200)
    Image = models.ImageField(upload_to='pics/client')

    def __str__(self):
        return self.Company


class Testimonial(models.Model):
    Name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Photo = models.ImageField(upload_to='pics/testimonial')
    Review = models.TextField()

    def __str__(self):
        return self.Name + " | " + self.Designation


class Team(models.Model):
    Name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Photo = models.ImageField(upload_to='pics/teams')

    Instagram = models.CharField(max_length=100, null=True, blank=100)
    LinkedIn = models.CharField(max_length=100, null=True, blank=100)
    Twitter = models.CharField(max_length=100, null=True, blank=100)
    Facebook = models.CharField(max_length=100, null=True, blank=100)

    def __str__(self):
        return self.Name + " | " + self.Designation


class Service(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField()
    Icon = models.ImageField(upload_to='pics/services')

    def __str__(self):
        return self.Name


class Blog(models.Model):
    Title = models.CharField(max_length=250)
    Image = models.ImageField(upload_to='pics/blog')
    Content = FroalaField()
    Date = models.DateField(null=True, blank=True)
    Tag_1 = models.CharField(max_length=50, blank=True, null=True)
    Tag_2 = models.CharField(max_length=50, blank=True, null=True)
    Tag_3 = models.CharField(max_length=50, blank=True, null=True)
    Tag_4 = models.CharField(max_length=50, blank=True, null=True)
    Tag_5 = models.CharField(max_length=50, blank=True, null=True)
    Tag_6 = models.CharField(max_length=50, blank=True, null=True)
    Tag_7 = models.CharField(max_length=50, blank=True, null=True)
    Tag_8 = models.CharField(max_length=50, blank=True, null=True)
    
    slug = models.SlugField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.Title


    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.Title)
        super(Blog, self).save(*args, **kwargs)


class WebsiteDetail(models.Model):
    title = models.CharField(max_length=250)
    home_title = models.CharField(max_length=100)
    home_heading = models.CharField(max_length=25)
    home_heading_1 = models.CharField(max_length=25)
    home_heading_2 = models.CharField(max_length=25)
    home_heading_3 = models.CharField(max_length=25)
    home_description = models.CharField(max_length=250)
    who_are_we_icon_heading = models.CharField(max_length=100)
    who_are_we_heading_1 = models.CharField(max_length=100)
    who_are_we_heading_2 = models.CharField(max_length=100)
    who_are_we_text = models.TextField()
    who_are_we_check_1 = models.CharField(max_length=50)
    who_are_we_check_2 = models.CharField(max_length=50)
    service_icon_heading = models.CharField(max_length=100)
    service_heading_1 = models.CharField(max_length=50)
    service_heading_2 = models.CharField(max_length=50)
    service_text = models.TextField()
    team_heading_1 = models.CharField(max_length=100)
    team_heading_2 = models.CharField(max_length=100)
    team_text = models.TextField()
    testimonial_heading_1 = models.CharField(max_length=100)
    testimonial_heading_2 = models.CharField(max_length=100)
    testimonial_text = models.TextField()
    blog_text = models.TextField()
    contact_heading = models.CharField(max_length=100)
    contact_desc =  models.CharField(max_length=250)
    contact_phone = models.CharField(max_length=20)
    contact_email = models.CharField(max_length=50)
    contact_address = models.CharField(max_length=100)
    linked_by_name = models.CharField(max_length=16)

    def __str__(self):
        return self.linked_by_name

