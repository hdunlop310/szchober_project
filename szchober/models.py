from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,blank=True,null=True)
    #username = models.CharField(max_length=20, default='')
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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,blank=True,null=True)
    #username = models.CharField(max_length=20, default='')
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
    feedback_id = models.CharField(max_length=10, unique=True, default='')
    description = models.CharField(max_length=500, default='')

    class Meta:
        verbose_name_plural = 'Feedback'

    def __str__(self):
        return self.feedback_id


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
