from szchober.models import UserProfile, Rider, Driver
from django.core import serializers


data = serializers.serialize('xml', Driver.objects.all())
