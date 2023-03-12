from django.shortcuts import render
from cart import cart
from django.http import HttpResponseRedirect
from checkout import checkout
def show_cart(request, template_name='cart/cart.html'):
    #if remove or update buttons from the cart are pressed then act accordingly
    if request.method == 'POST':
        postdata = request.POST.copy()
        if postdata['submit'] == 'Remove':
            cart.remove_from_cart(request)
        if postdata['submit'] == 'Update':
            cart.update_cart(request)

        if postdata['submit'] == 'Checkout':
            checkout_url = checkout.get_checkout_url(request)
            return HttpResponseRedirect(checkout_url)
        if postdata['submit'] == 'Mpesa':
            checkout_url2 = checkout.get_checkout_url2(request)
            return HttpResponseRedirect(checkout_url2)

    cart_items = cart.get_cart_items(request)
    cart_subtotal = cart.cart_subtotal(request)
    page_title = 'Shopping Cart'
    return render(request, template_name, locals())



# Create your views here.
