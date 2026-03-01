from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Service, Project, TeamMember, Testimonial, WhyChooseUs, CoreValue, Post, FAQ
from .forms import ContactForm


def home_view(request):
    services = Service.objects.filter(is_featured=True)[:4]
    projects = Project.objects.filter(is_featured=True)[:6]
    testimonials = Testimonial.objects.filter(is_active=True)[:6]
    why_choose_us_items = WhyChooseUs.objects.all()
    context = {
        'services': services,
        'projects': projects,
        'testimonials': testimonials,
        'why_choose_us_items': why_choose_us_items,
    }
    return render(request, 'home.html', context)


def about_view(request):
    team_members = TeamMember.objects.all()
    core_values = CoreValue.objects.all()
    context = {
        'team_members': team_members,
        'core_values': core_values,
    }
    return render(request, 'about.html', context)


def services_view(request):
    services = Service.objects.all()
    faqs = FAQ.objects.filter(is_active=True)
    context = {
        'services': services,
        'faqs': faqs,
    }
    return render(request, 'services.html', context)


def service_detail_view(request, slug):
    service = get_object_or_404(Service, slug=slug)
    other_services = Service.objects.exclude(pk=service.pk)[:4]
    context = {
        'service': service,
        'other_services': other_services,
    }
    return render(request, 'service_detail.html', context)


def projects_view(request):
    category = request.GET.get('category', '')
    projects = Project.objects.all()
    if category:
        projects = projects.filter(category=category)
    context = {
        'projects': projects,
        'current_category': category,
        'categories': Project.CATEGORY_CHOICES,
    }
    return render(request, 'projects.html', context)


def project_detail_view(request, slug):
    project = get_object_or_404(Project, slug=slug)
    related_projects = Project.objects.filter(category=project.category).exclude(pk=project.pk)[:3]
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'project_detail.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            
            # Send Email Automation
            from django.core.mail import send_mail
            from django.conf import settings
            
            subject = f"New Contact Inquiry: {inquiry.subject}"
            message = f"New inquiry received from {inquiry.name} ({inquiry.email}).\nPhone: {inquiry.phone}\n\nMessage:\n{inquiry.message}"
            
            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL], # Sends notification to company
                    fail_silently=True,
                )
            except Exception as e:
                pass # Fail silently for now
                
            messages.success(request, 'Thank you for your message! We\'ll get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)


from django.core.paginator import Paginator

def blog_list_view(request):
    post_list = Post.objects.filter(is_published=True)
    category = request.GET.get('category')
    if category:
        post_list = post_list.filter(category=category)
        
    paginator = Paginator(post_list, 6) # Show 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'categories': Post.CATEGORY_CHOICES,
        'current_category': category,
    }
    return render(request, 'blog_list.html', context)


def blog_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    related_posts = Post.objects.filter(category=post.category, is_published=True).exclude(pk=post.pk)[:3]
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'blog_detail.html', context)
