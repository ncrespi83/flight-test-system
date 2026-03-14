from django.contrib import admin
from .models import Requirement, TestPlan, TestEvent, TestPoint

# Register your models here.
admin.site.register([Requirement, TestPlan, TestEvent, TestPoint])

