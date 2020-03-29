from django.contrib import admin
from szchober.models import Driver, Rider, Rating, Feedback, Lift, CustomUser, UserDetails, MyUUIDModel
from szchober.models import UserProfile
# Register your models here.
admin.site.register(Driver)
admin.site.register(Rider)
admin.site.register(Rating)

admin.site.register(Feedback)
admin.site.register(Lift)

admin.site.register(UserProfile)
admin.site.register(CustomUser)
admin.site.register(UserDetails)
admin.site.register(MyUUIDModel)