from django.db import models

# Create your models here.
class recipe(models.Model):
    title=models.TextField()
    instructions=models.TextField()
    image=models.TextField()
    ingredients=models.TextField()
    image_link=models.TextField()


