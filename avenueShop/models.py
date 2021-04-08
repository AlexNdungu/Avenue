from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Genre(models.Model):
    genres = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.genres


class Movies(models.Model):
    MY_TYPE = (
        ('Movie','Movie'),
        ('Series','Series'),
    )

    movie = models.CharField(max_length=100, primary_key=True)
    genres = models.ForeignKey(Genre, on_delete=models.CASCADE)
    slength = models.IntegerField( null=True,verbose_name="Series_Length",blank=True)
    mlength = models.IntegerField( null=True,verbose_name="Movie_Length",blank=True)
    description = models.TextField(null=True,verbose_name="Description")
    banner = models.ImageField(upload_to='images')
    my_type = models.CharField( max_length=50, choices=MY_TYPE)

    def __str__(self):
        return self.movie

    class Meta:
        ordering= ['movie']     

    def get_absolute_url(self):
        return reverse ('avenueShop:createMovie',args=[self.id,])    
        