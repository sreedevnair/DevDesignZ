from django.shortcuts import render
from django.core.mail import send_mail
from .models import Client, Testimonial, Team, Service, Blog, WebsiteDetail
from django.conf import settings

# Create your views here.

def error_404_view(request, exception):
    return render(request, '404.html')

def error_500_view(request, *args, **argv):
    return render(request, '404.html')


def index(request):
    client = Client.objects.all()
    testimonial = Testimonial.objects.all()
    team = Team.objects.all()
    service = Service.objects.all()
    blog = Blog.objects.all()[::-1]
    website = WebsiteDetail.objects.get(linked_by_name='Website Details')

    if request.method == "POST":
        message_name = request.POST['name']
        message_phone = request.POST['phone']
        message_email = request.POST['email']
        message_subject = request.POST['subject']
        message_message = request.POST['message']
        email = settings.EMAIL_HOST_USER

        send_mail(
            message_subject + " | " + message_name, # subject
            message_message + "\n\nPhone : " + message_phone + "\nEmail : " + message_email , # message
            email, # from email 
            ['sreedevnair02@gmail.com', 'devdesignz02@gmail.com'], # to email
        )

        return render(request, 'index.html', {'Clients':client, 'message_name':message_name, 'Testimonials': testimonial, 'Teams':team, 'Service':service, 'Blogs':blog, 'website':website})
    else:
        return render(request, 'index.html', {'Clients':client, 'Testimonials': testimonial, 'Teams':team, 'Service':service, 'Blogs':blog, 'website':website})

    
def blog(request, blog_slug):
    blog = Blog.objects.get(slug=blog_slug)
    blogs = Blog.objects.all()[::-1][:3]

    return render(request, 'blog.html', {'blog':blog, 'blogs':blogs})


def blogs(request):
    blogs = Blog.objects.all()[::-1]

    return render(request, 'blogs.html', {'blogs':blogs})