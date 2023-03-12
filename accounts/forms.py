from django import forms
from accounts.models import UserProfile
from django.contrib.auth.forms import UserCreationForm

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

class RegistrationForm(UserCreationForm):
    password1 = forms.RegexField(label="Password", regex=r'^(?=.*\W+).*$',
                                 help_text='Password must be 8 characters long'
                                           'and contain at least one non-alphanumeric character i.e @#|>. ',
                                 widget=forms.PasswordInput, min_length=8)
    password2 = forms.RegexField(label="Confirm Password", regex=r'^(?=.*\W+).*$',
                                 help_text='Must be the same as above',
                                 widget=forms.PasswordInput, min_length=8)
    email = forms.CharField(max_length='50')