from django.test import TestCase
from szchober.models import Driver, Rider, Lift, Feedback, Rating


# Create your tests here.

class DriverModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Driver.objects.create(forename='forename', surname='surname',
                              password='password', email='mail@mail.com',
                              phone_number='07895462497', rating=5,
                              review='Theyre good', driver_id='driverid',
                              car_make='car make', car_model='carmodel',
                              car_registration='SF54 SRC', availability=True,
                              is_driver=True)

    def setUp(self):
        pass

    def test_forename_label(self):
        driver_forename = Driver.objects.get(id=1)
        field_label = driver_forename._meta.get_field('forename').verbose_name
        self.assertEquals(field_label, 'forename')

    def test_surname_label(self):
        driver_surname = Driver.objects.get(id=1)
        field_label = driver_surname._meta.get_field('surname').verbose_name
        self.assertEquals(field_label, 'surname')

    def test_password_label(self):
        driver_password = Driver.objects.get(id=1)
        field_label = driver_password._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

    def test_email_label(self):
        driver_email = Driver.objects.get(id=1)
        field_label = driver_email._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_email_label(self):
        driver_email = Driver.objects.get(id=1)
        field_label = driver_email._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_phone_number_label(self):
        driver_phone_number = Driver.objects.get(id=1)
        field_label = driver_phone_number._meta.get_field('phone_number').verbose_name
        self.assertEquals(field_label, 'phone number')

    def test_rating_label(self):
        driver_rating = Driver.objects.get(id=1)
        field_label = driver_rating._meta.get_field('rating').verbose_name
        self.assertEquals(field_label, 'rating')

    def test_review_label(self):
        driver_review = Driver.objects.get(id=1)
        field_label = driver_review._meta.get_field('review').verbose_name
        self.assertEquals(field_label, 'review')

    def test_driver_id_label(self):
        driver_driver_id = Driver.objects.get(id=1)
        field_label = driver_driver_id._meta.get_field('driver_id').verbose_name
        self.assertEquals(field_label, 'driver id')

    def test_car_make_label(self):
        driver_car_make = Driver.objects.get(id=1)
        field_label = driver_car_make._meta.get_field('car_make').verbose_name
        self.assertEquals(field_label, 'car make')

    def test_car_model_label(self):
        driver_car_model = Driver.objects.get(id=1)
        field_label = driver_car_model._meta.get_field('car_model').verbose_name
        self.assertEquals(field_label, 'car model')

    def test_car_model_label(self):
        driver_car_registration = Driver.objects.get(id=1)
        field_label = driver_car_registration._meta.get_field('car_registration').verbose_name
        self.assertEquals(field_label, 'car registration')

    def test_availability_label(self):
        driver_availability = Driver.objects.get(id=1)
        field_label = driver_availability._meta.get_field('availability').verbose_name
        self.assertEquals(field_label, 'availability')

    def test_is_driver_label(self):
        driver_is_driver = Driver.objects.get(id=1)
        field_label = driver_is_driver._meta.get_field('is_driver').verbose_name
        self.assertEquals(field_label, 'is driver')


class RiderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Rider.objects.create(forename='forename', surname='surname',
                             password='password', email='mail@mail.com',
                             phone_number='07895462497', rating=5,
                             review='Theyre good', rider_id='riderid',
                             address='address', postcode='G71 YUS',
                             is_rider=True)

    def setUp(self):
        pass

    def test_forename_label(self):
        rider_forename = Rider.objects.get(id=1)
        field_label = rider_forename._meta.get_field('forename').verbose_name
        self.assertEquals(field_label, 'forename')

    def test_surname_label(self):
        rider_surname = Rider.objects.get(id=1)
        field_label = rider_surname._meta.get_field('surname').verbose_name
        self.assertEquals(field_label, 'surname')

    def test_password_label(self):
        rider_password = Rider.objects.get(id=1)
        field_label = rider_password._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

    def test_email_label(self):
        rider_email = Rider.objects.get(id=1)
        field_label = rider_email._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_email_label(self):
        rider_email = Rider.objects.get(id=1)
        field_label = rider_email._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_phone_number_label(self):
        rider_phone_number = Rider.objects.get(id=1)
        field_label = rider_phone_number._meta.get_field('phone_number').verbose_name
        self.assertEquals(field_label, 'phone number')

    def test_rating_label(self):
        rider_rating = Rider.objects.get(id=1)
        field_label = rider_rating._meta.get_field('rating').verbose_name
        self.assertEquals(field_label, 'rating')

    def test_review_label(self):
        rider_review = Rider.objects.get(id=1)
        field_label = rider_review._meta.get_field('review').verbose_name
        self.assertEquals(field_label, 'review')

    def test_rider_id_label(self):
        rider_rider_id = Rider.objects.get(id=1)
        field_label = rider_rider_id._meta.get_field('rider_id').verbose_name
        self.assertEquals(field_label, 'rider id')

    def test_is_rider_label(self):
        rider_is_rider = Rider.objects.get(id=1)
        field_label = rider_is_rider._meta.get_field('is_rider').verbose_name
        self.assertEquals(field_label, 'is rider')


class LiftModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Lift.objects.create(lift_id='lift_id', start='start',
                            end='end', distance=4.53,
                            price=1.85)

    def setUp(self):
        pass

    def test_lift_id_label(self):
        lift_lift_id = Lift.objects.get(id=1)
        field_label = lift_lift_id._meta.get_field('lift_id').verbose_name
        self.assertEquals(field_label, 'lift id')

    def test_lift_start_label(self):
        lift_start = Lift.objects.get(id=1)
        field_label = lift_start._meta.get_field('start').verbose_name
        self.assertEquals(field_label, 'start')

    def test_lift_end_label(self):
        lift_end = Lift.objects.get(id=1)
        field_label = lift_end._meta.get_field('end').verbose_name
        self.assertEquals(field_label, 'end')

    def test_lift_distance_label(self):
        lift_distance = Lift.objects.get(id=1)
        field_label = lift_distance._meta.get_field('distance').verbose_name
        self.assertEquals(field_label, 'distance')

    def test_lift_price_label(self):
        lift_price = Lift.objects.get(id=1)
        field_label = lift_price._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'price')


class FeedbackModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Feedback.objects.create(feedback_id='feedback_id', description="good app")

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_feedback_id_label(self):
        feedback_feedback_id = Feedback.objects.get(id=1)
        field_label = feedback_feedback_id._meta.get_field('feedback_id').verbose_name
        self.assertEquals(field_label, 'feedback id')

    def test_feedback_description_label(self):
        feedback_description = Feedback.objects.get(id=1)
        field_label = feedback_description._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')


class RatingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Rating.objects.create(rating_id='rating_id', description="good app",
                                rating=5)

    def setUp(self):
        pass

    def test_rating_id_label(self):
        rating_rating_id = Rating.objects.get(id=1)
        field_label = rating_rating_id._meta.get_field('rating_id').verbose_name
        self.assertEquals(field_label, 'rating id')

    def test_rating_description_label(self):
        rating_description = Rating.objects.get(id=1)
        field_label = rating_description._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_rating_label(self):
        rating = Rating.objects.get(id=1)
        field_label = rating._meta.get_field('rating').verbose_name
        self.assertEquals(field_label, 'rating')
