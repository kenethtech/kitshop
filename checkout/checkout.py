import json

import requests
from requests.auth import  HTTPBasicAuth
from checkout import google_checkout
from cart import cart
from checkout.models import Order, OrderItem
from checkout.forms import CheckoutForm, MpesaPaymentForm
from checkout import authnet
from kitshop import settings
from django.urls import reverse
from checkout import mpesa_checkout
from accounts import profile
import urllib

#returns the URL from the checkout module for cart
def get_checkout_url(request):
    return reverse('checkout')
def get_checkout_url2(request):
    return reverse('mpesa_checkout')
def process(request):
    """Transaction results"""
    APPROVED = '1'
    DECLINED = '2'
    ERROR = '3'
    HELD_FOR_REVIEW = '4'
    postdata = request.POST.copy()
    card_num = postdata.get('credit_card_number','')
    exp_month = postdata.get('credit_card_expire_month','')
    exp_year = postdata.get('credit_card_expire_year','')
    exp_date = exp_month + exp_year
    cvv = postdata.get('credit_card_cvv','')
    amount = cart.cart_subtotal(request)
    results = {}
    response = authnet.do_aut_capture(amount=amount,card_num=card_num,exp_date=exp_date,card_cvv=cvv)
    if response[0]== APPROVED:
        transaction_id = response[6]
        order = create_order(request, transaction_id)
        results = {'order_number':order.id,'message':''}

    if response[0]== DECLINED:
        results = {'order_number':0, 'message': 'There is a problem with your credit card'}

    if response[0] == ERROR:
        results = {'order_number':0, 'message': 'Error processing your order.'}

    return results

def mpesa_process(request):
    postdata = request.POST.copy()
    phone_number = postdata.get('mpesa_phone_number')
    amount = cart.cart_subtotal(request)
    access_token = get_access_token()
    results ={}
    response = mpesa_checkout.mpesa_payment(phone_number, amount, access_token)
    if response['ResponseCode'] == '0':
        transaction_id = response['CheckoutRequestID']
        order = create_mpesa_order(request, transaction_id)
        results = {'order_number':order.id,'message':''}

    else:
        results = {'order_number': 0, 'message': 'Error processing your order.'}

    return results

def get_access_token():
    consumer_key = settings.MPESA_CONSUMER_KEY
    consumer_secrete = settings.MPESA_CUNSUMER_SECRET
    api_url = settings.MPESA_API_URL
    req = requests.get(api_url, auth =HTTPBasicAuth(consumer_key, consumer_secrete))
    acccess_token = json.loads(req.text)['access_token']
    return acccess_token

def create_mpesa_order(request, transaction_id):
    order = Order()
    checkout_form = MpesaPaymentForm(request.POST, instance=order)
    order = checkout_form.save(commit=False)
    order.transaction_id = transaction_id
    order.ip_address = request.META.get('REMOTE_ADDR')
    order.user = None
    if request.user.is_authenticated():
        order.user = request.user
    order.status = Order.SUBMITTED
    order.save()
    # if the orde save succeded
    if order.pk:
        cart_items = cart.get_cart_items(request)
        for ci in cart_items:
            oi = OrderItem()
            oi.order = order
            oi.quantity = ci.quantity
            oi.price = ci.price
            oi.product = ci.product
            oi.save()

        # all set, empty cart
        cart.empty_cart(request)

    #save profile infor for future orders
    if request.user.is_authenticated():
        profile.set(request)

    # return the new order
    return order

def create_order(request,transaction_id):
    order = Order()
    checkout_form = CheckoutForm(request.POST, instance=order)
    order = checkout_form.save(commit=False)
    order.transaction_id = transaction_id
    order.ip_address = request.META.get('REMOTE_ADDR')
    order.user = None
    if request.user.is_authenticated():
        order.user = request.user
    order.status = Order.SUBMITTED
    order.save()
    # if the orde save succeded
    if order.pk:
        cart_items = cart.get_cart_items(request)
        for ci in cart_items:
            oi = OrderItem()
            oi.order = order
            oi.quantity = ci.quantity
            oi.price = ci.price
            oi.product = ci.product
            oi.save()

        #all set, empty cart
        cart.empty_cart(request)

        # save profile infor for future orders
    if request.user.is_authenticated():
        profile.set(request)

    #return the new order
    return order

