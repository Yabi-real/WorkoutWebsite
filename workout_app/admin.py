from django.contrib import admin

# Register your models here.
from .models import Athelete
from .models import Workout
from .models import AtheleteProgess

admin.site.register(Athelete)
admin.site.register(Workout)
admin.site.register(AtheleteProgess)