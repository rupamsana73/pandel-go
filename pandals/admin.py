from django.contrib import admin
from .models import Pandal, Review
from .models import CrowdLevel


# Register  models here.
admin.site.register(Pandal)
admin.site.register(Review)
admin.site.register(CrowdLevel)


