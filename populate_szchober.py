import os 

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'szchober_project.settings')
from random import randint
import django

django.setup()
from szchober.models import User, Lift, Rating, Feedback


def populate():
    drivers = [{
                'forename': 'Jerri',
                'surname': 'Springer',
                'password': 'JerriSzchober10',
                'email': 'jerri@mail.com',
                'phone_number': '07568246221',
                'rating': 5,
                'review': 'She is a very good driver, always arrives on time and is a safe driver',
                'driver_id': 'd185694356',
                'car_make': 'Ford',
                'car_model': 'Fiesta',
                'car_registration': 'SD10 SYU',
                'availability': True}]

    riders = [{
               'forename': 'Johnny',
               'surname': 'Dunkin',
               'password': 'DunkSzchober10',
               'email': 'dunkinJ@mail.com',
               'phone_number': '07568912456',
               'rating': 4,
               'review': 'He is a good rider',
               'address': '13 Caithness St, Glasgow',
               'postcode': 'G207SB',
               'rider_id': 'r434641346'},

              {
               'forename': 'Romi',
               'surname': 'Schzil',
               'password': 'RSchnizzle34',
               'email': 'Schzil@mail.com',
               'phone_number': '07556894521',
               'rating': 2,
               'review': 'She is quite rude',
               'address': 'Glasgow University',
               'postcode': 'G128QQ',
               'rider_id': 'r568945236'}
              ]

    lifts = [
        {'lift_id': 'l286528641',
         'start': 'G67 UAD',
         'end': 'G71 2AC',
         'distance': 6,
         'price': 3.12}
    ]

    feedback =[
            {'feedback id' : 'f523985729','description': 'This app is very good'},
            {'feedback id' : 'f213124123','description': 'This app is good'},
            {'feedback id' : 'f213124123','description': 'This app barely alright'}
                ]
    rating = [
        {'rating id' : 'ra13733874',
        'description': 'very good',
        'rating': 5}
    ]

    for driver in drivers:
        d = add_driver(driver['forename'], driver['surname'], driver['password'], driver['email'],
                       driver['phone_number'], driver['rating'], driver['review'], driver['driver_id'],
                       driver['car_make'], driver['car_model'], driver['car_registration'], driver['availability'])

    for rider in riders:
        r = add_rider(rider['forename'], rider['surname'], rider['password'], rider['email'],
                      rider['phone_number'], rider['rating'], rider['review'], rider['address'],
                      rider['postcode'], rider['rider_id'])

    for lift in lifts:
        l = add_lift(lift['lift_id'], lift['start'], lift['end'], lift['distance'], lift['price'])

    for fd in feedback:
        f = add_feedback(fd['feedback_id'], fd['description'])

    for rat in rating:
        ra = add_rating(rat['rating_id'], rat['description'], rat['rating'])


def add_driver(forename, surname, password, email, phone_number, rating, review, driver_id,
               car_make, car_model, car_registration, availability):
    d = Driver.objects.get_or_create(forename=forename, surname=surname, password=password,
                                     email=email,
                                     phone_number=phone_number,
                                     rating=rating, review=review, driver_id=driver_id, car_make=car_make,
                                     car_model=car_model,
                                     car_registration=car_registration, availability=availability)[0]
    d.save()
    return d

    for us, user_data in users.items():
        u = add_user(us, user_data[''])

def add_rider(forename, surname, password, email, phone_number, rating, review, address, postcode, rider_id):
    r = \
        Rider.objects.get_or_create(forename=forename, surname=surname, password=password,
                                    email=email,
                                    phone_number=phone_number,
                                    rating=rating, review=review, address=address, postcode=postcode,
                                    rider_id=rider_id)[0]
    r.save()
    return r


def add_lift(lift_id, start, end, distance, price):
    l = Lift.objects.get_or_create(lift_id=lift_id, start=start, end=end, distance=distance, price=price)[0]
    l.save()
    return l


def add_feedback(feedback_id, description):
    f = Feedback.objects.get_or_create(feedback_id=feedback_id, description=description)[0]
    f.save()
    return f


def add_rating(rating_id, description, rating):
    ra = Rating.objects.get_or_create(rating_id=rating_id, description=description, rating=rating)[0]
    ra.save()
    return ra


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()


