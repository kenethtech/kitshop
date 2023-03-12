from django import template
from cart import cart
from django.template.loader import get_template
from catalog.models import Category
from django.contrib.flatpages.models import FlatPage
register = template.Library()

temp = get_template('tags/cart_box.html')

@register.inclusion_tag(temp)
def cart_box(request):
    cart_item_count = cart.cart_distinct_item_count(request)
    return {'cart_item_count': cart_item_count}

t= get_template('tags/category_list.html')
@register.inclusion_tag(t)
def category_list(request_path):
    active_categories = Category.active.all()
    return {
        'active_categories': active_categories,
        'request_path':request_path
    }
temp2 = get_template('tags/footer.html')
@register.inclusion_tag(temp2)
def footer_links():
    flatpage_list = FlatPage.objects.all()
    return {'flatpage_list': flatpage_list}

temp3 = get_template('tags/product_list.html')
@register.inclusion_tag(temp3)
def product_list(products, header_text):
    return {'products': products,
            'header_text': header_text}