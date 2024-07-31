from django.db import models

# Create your models here.
class TestUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    

class GeneratedImage(models.Model):
    prompt = models.CharField(max_length=255)
    filename = models.CharField(max_length=255, default='default_filename.webp')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prompt