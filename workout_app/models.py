from django.db import models

from django.urls import reverse

class AtheleteProgess(models.Model):
    title = models.CharField(max_length=200)
    contact_email = models.CharField("Contact Email", max_length=200)
    is_active = models.BooleanField(default=False)
    about = models.TextField(blank=True, null= True)
    
   
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('sport-detail', args=[str(self.id)])

# Create your models here.
class Athelete(models.Model):


    SPORT = (
    ('Track and Field'),
    #('Swimming'),
    ('Basketball'),
    #('Tennis'),
    #('Football'),
    #('Soccer')
    ),

    name = models.CharField(max_length=200)
    email = models.CharField("Email", max_length=200)
    sport = models.CharField(max_length=200, choices=SPORT, blank = False)

    athelete_progess = models.OneToOneField(AtheleteProgess, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('athelete-detail', args=[str(self.id)])



class Workout(models.Model):
    title = models.CharField(max_length=200, null=True, default=None)
    description = models.TextField(max_length=200, blank=True, null=True, default=None)
    athelete_progess = models.ForeignKey(AtheleteProgess, on_delete=models.CASCADE, default=None)
   
   # Protfolio = models.CharField(max_length=140, default=None)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('athelete-detail-workout', args=[str(self.id)])
    



 