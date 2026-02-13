#mini_insta/models.py

from django.db import models

# Create your models here.
class Profile(models.Model):
    '''Encapsulates a user profile.'''


    #define the attribute of the profile
    username = models.TextField(blank=False)
    display_name = models.TextField(blank=True)
    profile_image = models.TextField(blank=True)
    profile_image_url = models.TextField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateTimeField(auto_now=True)