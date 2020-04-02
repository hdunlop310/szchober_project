from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

'''
----------------------------------------------------------------------------------------------------------------
 models.py file - Szchober database
There are multiple models in this database
I have created a CustomUser model that allows for a cusomised version of the provided User model from Django
- CustomUser, User and UserProfile all relate to the user creating their own user account
- The Driver and Rider models are the two user models. There are two user models as different user 
    information is needed depending on the user type. If a user is a "Driver" then their address and postcode
    is not needed. Instead, they must provide their car make and model and their registration number.
    However, if a user is a Rider, they should not have to provide vehicle information. Instead they need 
    to provide their address and postcode so that a driver can collect them.
    
- The Lift model stores the data relating to the data that is needed when a rider chooses such as the start destination,
    end destination, total distance and price
    
- The Feedback model is to do with the user's feedback on Szchober - their comment and rating is stored so 
    that it is easily read.
    
- The Rating Model is stores a user's rating on another user.  

----------------------------------------------------------------------------------------------------------------
'''


# Create your models here.

class CustomUser(AbstractUser):
    type_choices = (
        ('D', 'Driver'),
        ('R', 'Rider'),

    )
    user_type = models.CharField(max_length=1,
                                 choices=type_choices,
                                 default='')


class UserDetails(models.Model):
    type = models.OneToOneField('CustomUser', on_delete=models.CASCADE)


class Driver(AbstractBaseUser):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    # username = models.CharField(max_length=20, default='')
    forename = models.CharField(max_length=16, default='')
    surname = models.CharField(max_length=16, default='')
    password = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=30, unique=True, default='')
    phone_number = models.CharField(max_length=11, default='')
    rating = models.IntegerField(default=5)
    review = models.CharField(max_length=128, default='')
    driver_id = models.CharField(max_length=10, unique=True, default='')
    car_make = models.CharField(max_length=10, default='')
    car_model = models.CharField(max_length=10, default='')
    car_registration = models.CharField(max_length=8, unique=True, default='')
    availability = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=True)

    USERNAME_FIELD = 'driver_id'

    def __str__(self):
        return self.driver_id


class Rider(AbstractBaseUser):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    # username = models.CharField(max_length=20, default='')
    forename = models.CharField(max_length=16, default='')
    surname = models.CharField(max_length=16, default='')
    password = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=30, unique=True, default='')
    phone_number = models.CharField(max_length=11, default='')
    rating = models.IntegerField(default=5)
    review = models.CharField(max_length=128, default='')
    address = models.CharField(max_length=128, default='')
    postcode = models.CharField(max_length=7, default='')
    rider_id = models.CharField(max_length=10, unique=True, default='')
    is_rider = models.BooleanField(default=True)

    USERNAME_FIELD = 'rider_id'

    def __str__(self):
        return self.rider_id


class Lift(models.Model):
    lift_id = models.CharField(max_length=10, unique=True, default='')
    start = models.CharField(max_length=10, default='')
    end = models.CharField(max_length=10, default='')
    distance = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.lift_id


class Feedback(models.Model):
    # feedback_id = models.CharField(max_length=10, unique=True, default='')
    name = models.CharField(max_length=20, default='')
    description = models.TextField(max_length=500, default='')

    class Meta:
        verbose_name_plural = 'Feedback'

    #def __str__(self):
     #   return self.feedback_id


class Rating(models.Model):
    rating_id = models.CharField(max_length=10, unique=True, default='')
    description = models.CharField(max_length=500, default='')
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.rating_id


class User(models.Model):
    is_rider = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return "User"
