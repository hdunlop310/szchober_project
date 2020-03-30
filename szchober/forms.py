from django.contrib.auth.models import User
from szchober.models import UserProfile, Rider, Driver
from django import forms


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
