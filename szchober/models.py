from django.db import models


# Create your models here.
class User(models.Model):
    forename = models.CharField(max_length=16)
    surname = models.CharField(max_length=16)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=11)
    rating = models.IntegerField(default=5)
    review = models.CharField(max_length=128)
    user_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

    class Rider(models.Model):
        address = models.CharField(max_length=128)
        postcode = models.CharField(max_length=7)
        rider_id = models.CharField(max_length=10, unique=True)

        def __str__(self):
            return self.name

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
        return self.name
