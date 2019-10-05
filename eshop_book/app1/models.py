from django.db import models

# Create your models here.
class Book(models.Model):
    #title price author full text file
    title = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return '{} {} $'.format(self.title,self.price)