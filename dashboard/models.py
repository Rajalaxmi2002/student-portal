from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) 
    description = models.TextField()
    
    def __str__(self):  # Corrected double underscores here
        return self.title

    class Meta:
        verbose_name = "note"
        verbose_name_plural = "notes"

    
   