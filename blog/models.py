from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField(max_length = 300)


    def __str__(self):
        return self.title
