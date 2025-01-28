from django.contrib import admin

# Register your models here.
from .models import Employees
from .models import Division
from .models import PersonalInfo
from .models import LearningCourse

admin.site.register(Employees)
admin.site.register(Division)
admin.site.register(PersonalInfo)
admin.site.register(LearningCourse)