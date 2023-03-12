from django.shortcuts import render, get_object_or_404, HttpResponse
from catalog.models import Category, Product
from stats import stats
from kitshop.settings import PRODUCTS_PER_ROW
from django.urls import reverse
from cart import cart
from django.http import HttpResponseRedirect
from . forms import ProductAddToCartForm



def index(request, template_name ="catalog/index.html"):
    search_recs = stats.recommended_from_search(request)
    featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    recently_viewed = stats.get_recently_viewed(request)
    view_recs = stats.recommend_from_views(request)
    page_title = 'Sports equipments Shop'
    return render(request, template_name, locals())

def show_category(request, category_slug, template_name="catalog/category.html"):
    c = get_object_or_404(Category, slug= category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description

    return render(request, template_name, locals())
# product view with POST vs GET detection
def show_product(request, product_slug, template_name="catalog/product.html"):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.all()
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    from stats import stats
    stats.log_product_view(request, p)
    #need to evaluate the HTTP method

    if request.method == 'POST':
        #add to cart...create the bound form
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        #check if posted date is valid
        if form.is_valid():
            #add to cart and redirect to cart page
            cart.add_to_cart(request)
            #if test cookie worked get rid of it
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

            url = reverse('show_cart')
            return HttpResponseRedirect(url)

    else:
        # its a GET, create the unbound form. note request as a kwarg
        form = ProductAddToCartForm(request=request, label_suffix=':')
    #assign the hidden input the product slug

    form.fields['product_slug'].widget.attrs['value'] = product_slug

    #set the set cookie on  our first GET request
    request.session.set_test_cookie()

    return render(request, template_name, locals())

def all_products(request, template_name="catalog/all_products.html"):
    products = Product.active.all()
    page_title = 'Products'

    return render(request, template_name, locals())


# Create your views here.
