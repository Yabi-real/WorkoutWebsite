from django.forms import ModelForm
from .models import Athelete, AtheleteProgess, Workout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields =('title', 'description',)

class AtheleteProgessForm(ModelForm):
    class Meta:
        model = AtheleteProgess
        fields =('title', 'contact_email','is_active','about',)

class AtheleteForm(ModelForm):
    class Meta:
        model = Athelete
        fields =('name', 'email' ,'sport', 'athelete_progess')
