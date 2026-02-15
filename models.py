#mini_insta/models.py

# Create your models here.
from django.db import models
class Profile(models.Model):
    """Encapsulates a user profile."""
    
    username = models.CharField(max_length=50, unique=True)
    display_name = models.CharField(max_length=100)
    profile_image_url = models.URLField(blank=True)
    bio_text = models.TextField(blank=True, max_length=500)
    join_date = models.DateField()
    
    def __str__(self):
        """Return a string representation of this Profile."""
        return f'{self.username}'
