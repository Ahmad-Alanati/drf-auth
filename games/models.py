from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=255)
    purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    price = models.SmallIntegerField(default=30)
    description = models.TextField()
    released_date = models.DateTimeField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']