from .models import CompanyInfo

def company_info(request):
    """
    Context processor to make company info available to all templates globally.
    """
    return {
        'company_info': CompanyInfo.objects.first()
    }
