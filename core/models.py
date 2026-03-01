from django.db import models
from django.utils.text import slugify


class Service(models.Model):
    """Services offered by Kelstech Systems."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    icon_class = models.CharField(
        max_length=100, 
        help_text="Font Awesome or SVG icon class, e.g. 'fa-shield-halved'",
        default='fa-cog'
    )
    short_description = models.TextField(max_length=300)
    full_description = models.TextField(blank=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # SEO / OG Tags
    meta_title = models.CharField(max_length=60, blank=True, help_text='SEO title (max 60 chars)')
    meta_description = models.CharField(max_length=160, blank=True, help_text='SEO description (max 160 chars)')
    og_image = models.ImageField(upload_to='seo/', blank=True, null=True, help_text='Image for social sharing')

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Project(models.Model):
    """Portfolio projects / case studies."""
    CATEGORY_CHOICES = [
        ('cctv', 'CCTV & Security'),
        ('app', 'App Development'),
        ('web', 'Website Development'),
        ('software', 'Software Development'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(help_text="Short teaser description")
    full_description = models.TextField(blank=True, help_text="Detailed project study / story")
    image = models.ImageField(upload_to='projects/', blank=True, null=True, help_text="Main featured image")
    client_name = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='cctv')
    date_completed = models.DateField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # SEO / OG Tags
    meta_title = models.CharField(max_length=60, blank=True, help_text='SEO title (max 60 chars)')
    meta_description = models.CharField(max_length=160, blank=True, help_text='SEO description (max 160 chars)')
    og_image = models.ImageField(upload_to='seo/', blank=True, null=True, help_text='Image for social sharing')

    class Meta:
        ordering = ['-date_completed', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class ProjectImage(models.Model):
    """Gallery images for a project."""
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"Image for {self.project.title}"


class TeamMember(models.Model):
    """Team members of Kelstech Systems."""
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} — {self.role}"


class Testimonial(models.Model):
    """Client testimonials."""
    client_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    quote = models.TextField()
    rating = models.PositiveIntegerField(default=5, choices=[(i, str(i)) for i in range(1, 6)])
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.client_name} — {self.company}"


class ContactInquiry(models.Model):
    """Contact form submissions."""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Contact Inquiries'

    def __str__(self):
        return f"{self.name} — {self.subject}"


class CompanyInfo(models.Model):
    """Singleton model for company information and stats."""
    # Branding
    company_name = models.CharField(max_length=100, default='Kels Technologies & Systems', help_text='Name displayed on the website')
    company_logo = models.ImageField(upload_to='company/', blank=True, null=True, help_text='Main website logo')

    # About Us Page text
    about_headline = models.CharField(max_length=200, default='Built on Trust, Driven by Innovation')
    our_story = models.TextField(default='Founded with a vision to bridge the gap between security and technology...')
    mission = models.TextField(default='To provide world-class security and technology solutions...')
    vision = models.TextField(default='To be the most trusted name in security technology...')
    footer_description = models.TextField(default='Empowering businesses with cutting-edge security solutions and innovative technology services.', help_text='Brief description shown in the website footer')
    
    # Home Page Stats
    projects_completed = models.PositiveIntegerField(default=500)
    happy_clients = models.PositiveIntegerField(default=200)
    years_experience = models.PositiveIntegerField(default=10)
    team_members_count = models.PositiveIntegerField(default=50)

    # Contact Information
    address = models.CharField(max_length=255, default='Accra, Ghana')
    phone = models.CharField(max_length=50, default='+233 XX XXX XXXX')
    email = models.EmailField(default='info@kelstechsystems.com')
    working_hours = models.CharField(max_length=100, default='Mon - Fri: 8AM - 6PM')
    
    # Social Links & Chat
    facebook_url = models.URLField(blank=True, help_text='Facebook profile or page URL')
    twitter_url = models.URLField(blank=True, help_text='Twitter profile URL')
    instagram_url = models.URLField(blank=True, help_text='Instagram profile URL')
    linkedin_url = models.URLField(blank=True, help_text='LinkedIn profile URL')
    whatsapp_number = models.CharField(max_length=30, blank=True, help_text='Include country code without +, e.g. 233XXXXXXXXX', default='233XXXXXXXXX')

    # Global SEO / OG Tags (Homepage & Defaults)
    meta_title = models.CharField(max_length=60, blank=True, help_text='Global SEO title (max 60 chars)')
    meta_description = models.CharField(max_length=160, blank=True, help_text='Global SEO description (max 160 chars)')
    og_image = models.ImageField(upload_to='seo/', blank=True, null=True, help_text='Default image for social sharing')

    class Meta:
        verbose_name_plural = 'Company Info'

    def __str__(self):
        return "Company Information"

    def save(self, *args, **kwargs):
        self.pk = 1 # Ensure only one instance exists
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class WhyChooseUs(models.Model):
    """Why Choose Us items for the home page."""
    title = models.CharField(max_length=200)
    icon_class = models.CharField(max_length=100, default='fa-check', help_text="Font Awesome icon class")
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']
        verbose_name_plural = 'Why Choose Us Items'

    def __str__(self):
        return self.title


class CoreValue(models.Model):
    """Core values for the about page."""
    title = models.CharField(max_length=200)
    icon_class = models.CharField(max_length=100, default='fa-star')
    color_class = models.CharField(max_length=50, default='primary', help_text="Tailwind color prefix: primary, accent, green, yellow, etc.")
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class Post(models.Model):
    """Blog posts and insights."""
    CATEGORY_CHOICES = [
        ('security', 'Security Tips'),
        ('tech', 'Tech Trends'),
        ('company', 'Company News'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.CharField(max_length=100, default='Kelstech Team')
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='security')
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # SEO / OG Tags
    meta_title = models.CharField(max_length=60, blank=True, help_text='SEO title (max 60 chars)')
    meta_description = models.CharField(max_length=160, blank=True, help_text='SEO description (max 160 chars)')
    og_image = models.ImageField(upload_to='seo/', blank=True, null=True, help_text='Image for social sharing')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        from django.utils.text import slugify
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class FAQ(models.Model):
    """Frequently Asked Questions for the website."""
    question = models.CharField(max_length=300)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question
