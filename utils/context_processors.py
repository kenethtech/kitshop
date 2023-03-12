from catalog.models import Category
from kitshop import settings

def kitshop(request):
    return {
        'site_name': settings.SITE_NAME,
        'meta_keywords': settings.META_KEYWORDS,
        'meta_description': settings.META_DESCIPTION,
        'MEDIA_URL': settings.STATIC_URL,
        'request': request
    }