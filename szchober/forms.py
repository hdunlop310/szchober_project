from django.contrib.auth.models import User
from szchober.models import UserProfile, Rider, Driver, MyUUIDModel
from django import forms
import uuid


class UserFormDriver(forms.ModelForm):
   # driver_id = uuid.uuid4()
    password = forms.CharField(widget=forms.PasswordInput())
    #driver_id = Driver.objects.create(driver_id=driver_id)

    class Meta:
        model = Driver
        fields = ('forename', 'surname', 'email', 'password', 'phone_number',
                  'car_make', 'car_model', 'car_registration', )


class UserFormRider(forms.ModelForm):
    #rider_id = uuid.uuid4()
    password = forms.CharField(widget=forms.PasswordInput())
    #rider_id = Rider.objects.create(rider_id=rider_id)

    class Meta:
        model = Rider
        fields = ('forename', 'surname', 'email', 'password', 'phone_number', 'address', 'postcode',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
