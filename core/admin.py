from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Service, Project, ProjectImage, TeamMember, Testimonial, ContactInquiry, CompanyInfo, WhyChooseUs, CoreValue, Post, FAQ


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ('title', 'order', 'is_featured', 'created_at')
    list_editable = ('order', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'short_description')
    list_filter = ('is_featured',)


class ProjectImageInline(TabularInline):
    model = ProjectImage
    extra = 3


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ('title', 'category', 'client_name', 'is_featured', 'date_completed')
    list_editable = ('is_featured',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description', 'client_name')
    list_filter = ('category', 'is_featured')
    inlines = [ProjectImageInline]


@admin.register(TeamMember)
class TeamMemberAdmin(ModelAdmin):
    list_display = ('name', 'role', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'role')


@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ('client_name', 'company', 'rating', 'is_active', 'created_at')
    list_editable = ('is_active',)
    search_fields = ('client_name', 'company', 'quote')
    list_filter = ('is_active', 'rating')


@admin.register(ContactInquiry)
class ContactInquiryAdmin(ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'created_at')
    list_editable = ('is_read',)
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('is_read',)
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'created_at')


@admin.register(CompanyInfo)
class CompanyInfoAdmin(ModelAdmin):
    list_display = ('__str__', 'projects_completed', 'happy_clients', 'years_experience', 'team_members_count')
    
    def has_add_permission(self, request):
        # Prevent adding more than 1 instance
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(ModelAdmin):
    list_display = ('title', 'icon_class', 'order')
    list_editable = ('order', 'icon_class')


@admin.register(CoreValue)
class CoreValueAdmin(ModelAdmin):
    list_display = ('title', 'icon_class', 'color_class', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description')

@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_published', 'created_at')
    list_editable = ('is_published', 'category')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content', 'author')
    list_filter = ('is_published', 'category')
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'author', 'category', 'is_published', 'image')}),
        ('Content', {'fields': ('content',)}),
        ('SEO Options', {'fields': ('meta_title', 'meta_description', 'og_image'), 'classes': ('collapse',)}),
    )

@admin.register(FAQ)
class FAQAdmin(ModelAdmin):
    list_display = ('question', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    search_fields = ('question', 'answer')
