from django.contrib import admin
from szchober.models import Driver, Rider, Rating, Feedback, Lift, CustomUser, UserDetails
from szchober.models import UserProfile

'''
----------------------------------------------------------------------------------------------------------------
 admin.py file 
Registers the models in the database so they can be used

----------------------------------------------------------------------------------------------------------------
'''

# Register your models here.
admin.site.register(Driver)
admin.site.register(Rider)
admin.site.register(Rating)

admin.site.register(Feedback)
admin.site.register(Lift)

admin.site.register(UserProfile)
admin.site.register(CustomUser)
admin.site.register(UserDetails)
