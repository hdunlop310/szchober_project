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

class UserProfile(models.Model):
        # This line is required. Links UserProfile to a User model instance. user = models.OneToOneField(User, on_delete=models.CASCADE)
        # # The additional attributes we wish to include.
        # website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username

    class Rider(models.Model):
        address = models.CharField(max_length=128)
        postcode = models.CharField(max_length=7)
        rider_id = models.CharField(max_length=10, unique=True)

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

    class Driver(models.Model):
        driver_id = models.CharField(max_length=10, unique=True)
        car_make = models.CharField(max_length=10)
        car_model = models.CharField(max_length=10)
        car_registration = models.CharField(max_length=8, unique=True)
        availability = models.BooleanField()

        def __str__(self):
            return self.name


class Lift(models.Model):
    lift_id = models.CharField(max_length=10, unique=True)
    start = models.CharField(max_length=10)
    end = models.CharField(max_length=10)
    distance = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.name


class Feedback(models.Model):
    feedback_id = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Rating(models.Model):
    rating_id = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=500)
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
