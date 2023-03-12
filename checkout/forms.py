from django import forms
from checkout.models import Order
import datetime
import re

def cc_expire_years():
    current_year = datetime.datetime.now().year
    years =range(current_year, current_year+12)
    return [(str(x),str(x)) for x in years]

def cc_expire_month():
    months = []
    for month in range(1,13):
        if len(str(month)) == 1:
            numeric ='0' + str(month)
        else:
            numeric = str(month)
        months.append((numeric, datetime.date(2023, month, 1).strftime('%B')))
    return months

CARD_TRPES =(('Mastercard','Mastercard'),
             ('VISA','VISA'),
             ('AMEX','AMEX'),
             ('Discover','Discover'),)

def strip_non_numbers(data):
    """ gets rid of all nun numbers """
    non_numbers = re.compile('\D')
    return non_numbers.sub('',data)
#Gateway test credit cards won't pass this validation
def cardLuhnChecksumIsValid(card_number):
    """ chechs to make sure that the card passes luhn mod-10 checksum"""
    sum =0
    num_digits = len(card_number)
    oddeven = num_digits & 1
    for count in range(0, num_digits):
        digit = int(card_number[count])
        if not ((count & 1)^oddeven):
            digit = digit*2
        if digit > 9:
            digit = digit - 9
        sum = sum + digit

    return ((sum % 10) == 0)

class CheckoutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)
        #override default attributes
        for field in self.fields:
            self.fields[field].widget.attrs['size']='30'
        self.fields['shipping_state_or_county'].widget.attrs['size']='3'
        self.fields['shipping_state_or_county'].widget.attrs['size'] = '3'
        self.fields['shipping_zip'].widget.attrs['size'] = '6'
        self.fields['billing_state_or_county'].widget.attrs['size'] = '3'
        self.fields['billing_state_or_county'].widget.attrs['size'] = '3'
        self.fields['billing_zip'].widget.attrs['size'] = '6'
        self.fields['credit_card_type'].widget.attrs['size'] = '1'
        self.fields['credit_card_expire_year'].widget.attrs['size'] = '1'
        self.fields['credit_card_expire_month'].widget.attrs['size'] = '1'
        self.fields['credit_card_cvv'].widget.attrs['size'] = '5'

    class Meta:
        model = Order
        exclude = ('status', 'ip_address', 'user','transaction_id',)

    credit_card_number = forms.CharField()
    credit_card_type = forms.CharField(widget=forms.Select(choices=CARD_TRPES))
    credit_card_expire_month = forms.CharField(widget=forms.Select(choices=cc_expire_month()))
    credit_card_expire_year = forms.CharField(widget=forms.Select(choices=cc_expire_years()))
    credit_card_cvv = forms.CharField()

    def clean_credit_card_number(self):
        cc_number = self.cleaned_data['credit_card_number']
        stripped_cc_number = strip_non_numbers(cc_number)
        if not cardLuhnChecksumIsValid(stripped_cc_number):
            raise forms.ValidationError('The credit card you entered is invalid.')

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        stripped_phone = strip_non_numbers(phone)
        if len(stripped_phone) < 10:
            raise forms.ValidationError('Enter a valid phone number with area code.(e.g +254-70-000-0000)')
        return self.cleaned_data['phone']

class MpesaPaymentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MpesaPaymentForm, self).__init__(*args, **kwargs)
        #override default attributes
        for field in self.fields:
            self.fields[field].widget.attrs['size']='30'
        self.fields['shipping_state_or_county'].widget.attrs['size']='3'
        self.fields['shipping_state_or_county'].widget.attrs['size'] = '3'
        self.fields['shipping_zip'].widget.attrs['size'] = '6'
        self.fields['billing_state_or_county'].widget.attrs['size'] = '3'
        self.fields['billing_state_or_county'].widget.attrs['size'] = '3'
        self.fields['billing_zip'].widget.attrs['size'] = '6'
        self.fields['mpesa_phone_number'].widget.attrs['size'] = '26'


    class Meta:
        model = Order
        exclude = ('status', 'ip_address', 'user','transaction_id',)

    mpesa_phone_number = forms.CharField()


    def clean_mpesa_phone_number(self):
        phone_number = self.cleaned_data['mpesa_phone_number']
        stripped_phone_number = strip_non_numbers(phone_number)
        if len(stripped_phone_number) < 10:
            raise forms.ValidationError('Enter a valid phone number with area code.(e.g +254-70-000-0000)')
        return self.cleaned_data['phone']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        stripped_phone = strip_non_numbers(phone)
        if len(stripped_phone) < 10:
            raise forms.ValidationError('Enter a valid phone number with area code.(e.g +254-70-000-0000)')
        return self.cleaned_data['phone']