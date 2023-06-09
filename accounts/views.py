from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from checkout.models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from accounts.forms import UserProfileForm, RegistrationForm
from accounts import profile

def register(request, template_name="registration/register.html"):
    if request.method == 'POST':
        postdata = request.POST.copy()
        form =RegistrationForm(postdata)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.email = postdata.get('email','')
            new_user.save()
            user = postdata.get('username','')
            passw = postdata.get('password1','')
            auth_newuser = authenticate(username=user, password=passw)
            if auth_newuser and auth_newuser.is_active:
                login(request, new_user)
                url = reverse('my_account')
                return HttpResponseRedirect(url)


    else:
        form = RegistrationForm()
    page_title = 'User Registration'

    return render(request, template_name, locals())

@login_required
def my_account(request, template_name="registration/my_account.html"):
    page_title = 'My Account'
    orders = Order.objects.filter(user=request.user)
    name = request.user.username
    return render(request, template_name, locals())

@login_required
def order_details(request, order_id, template_name="registration/order_details.html"):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    page_title = 'Order Details for Order #' + order_id
    order_items = OrderItem.objects.filter(order=order)
    return render(request, template_name, locals())

@login_required
def order_info(request, template_name="registration/order_info.html"):
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = UserProfileForm(postdata)
        if form.is_valid():
            profile.set(request)
            url = reverse('my_account')
            return HttpResponseRedirect(url)
    else:
        user_profile = profile.retrieve(request)
        form = UserProfileForm(instance=user_profile)
    page_title = 'Edit Order Information'
    return render(request, template_name, locals())


# Create your views here.
