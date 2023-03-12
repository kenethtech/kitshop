from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from search import search
from kitshop import settings


def results(request, template_name="search/results.html"):
    word = request.GET.get('word', '')
    #get current page number. Set to 1 if missing or invalid
    try:
       page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1

    # retrieve the matching products
    matching = search.products(word).get('products')
    # generate the paginator object
    paginator = Paginator(matching, settings.PRODUCTS_PER_PAGE)
    try:
        results = paginator.page(page).object_list
    except (InvalidPage, EmptyPage):
        results =paginator.page(1).object_list

    #store the search into the database
    search.store(request, word)

    page_title = 'Search Results for:' + word

    return render(request, template_name, locals())
# Create your views here.
