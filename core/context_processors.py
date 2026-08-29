from .models import CompanyInfo, Service

def company_info(request):
    """
    Context processor to make company info and global services available to all templates.
    """
    return {
        'company_info': CompanyInfo.objects.first(),
        'global_services': Service.objects.all()[:6],
    }
