import urllib.parse
from django.template.loader import get_template
from django import template
from search.forms import SearchForm

register = template.Library()

temp1 = get_template("tags/search_box.html")
@register.inclusion_tag(temp1)
def search_box(request):
    word = request.GET.get('word','')
    form = SearchForm({'word': word})
    return {'form': form}

temp2 = get_template("tags/pagination_links.html")
@register.inclusion_tag(temp2)
def pagination_links(request, paginator):
    raw_params = request.GET.copy()
    page = raw_params.get('page',1)
    p = paginator.page(page)
    try:
        del raw_params['page']
    except KeyError:
        pass
    params = urllib.parse.urlencode(raw_params)
    return {'request': request,
            'paginator': paginator,
            'p': p,
            'params': params}
