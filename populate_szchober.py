import os 

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'szchober_project.settings')
from random import randint
import django

django.setup()
from szchober.models import User, Lift, Rating, Feedback

def add_ride(start,end,price,distance):
    liftid = randint(4,4)
    c = Lift.objects.get_or_create(liftid=liftid,start=start,end=end,price=price,distance=distance)[0]
    c.save()
    return c

def add_feedback(description):
    fid=randint(10,10)
    f = Feedback.objects.get_or_create(feedid=fid,description=description)[0]
    f.save()
    return f


def populate():
    users = [{'forename': 'Jerri',
            'surname': 'Springer',
            'password': 'jerrispassword',
            'email': 'jerri@gmail.com',
            'phone_number': '07234567834',
            'rating': 5,
            'review':'very good driver',
            'user id' : 'r0912357647',
            'type' : {'car make':'Ford',
            'car model': 'Fiesta',
            'car registration' : 'SD12 STX',
            'availability': True,
            'driver_id': 'r0912357647'}},

            {'forename': 'Johnny',
            'surname': 'Dunkin',
            'password': 'jdunk',
            'email': 'dunk@gmail.com',
            'phone_number': '0787654325',
            'rating': 2,
            'review':'ok rider',
            'user id' : 'd091247647',
            'type' : {'address':'10 Glasgow Drive',
            'postcode': 'G78 U18',
            'rider_id': 'd091247647'}},

            {'forename': 'Romi',
            'surname': 'Schzil',
            'password': 'romi1980',
            'email': 'r80@gmail.com',
            'phone_number': '07523756233',
            'rating': 1,
            'review':'bad rider',
            'user id' : 'd923257647',
            'type' : {'address':'5 Django Lane',
            'postcode': 'G67 UAD',
            'rider_id': 'd923257647'}}
        ]

    lift = [
        {'lift id': 'l286528641',
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


    for us, user_data in users.items():
        u = add_user(us, user_data[''])

    for feedback,feedback_disc in feedback.items():
        f=add_feedback(feedback,feedback_disc)

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()


