from django.contrib.auth.models import User
from szchober.models import UserProfile, Rider, Driver
from django import forms

'''
----------------------------------------------------------------------------------------------------------------
 forms.py file - Creates forms for both user types so they can log in and create an account
 - UserFormDriver - ties to the Driver model, allows user to create password and takes 
    in the relevant data that a driver user must give.
- UserFormRider - ties to the Rider model, allows user to create password and takes
    in the relevant data that a rider user must give
- UserProfileForm - ties to the UserProfile model, allows users to upload a picture.

----------------------------------------------------------------------------------------------------------------
'''

class UserFormDriver(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Driver
        fields = ('forename', 'surname', 'email', 'password', 'phone_number',
                  'car_make', 'car_model', 'car_registration', 'driver_id',)


class UserFormRider(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Rider
        fields = ('forename', 'surname', 'email', 'password', 'phone_number', 'address', 'postcode',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
