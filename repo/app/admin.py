from django.contrib import admin

from app.models import UserProfile
from app.models import Report


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Report)
