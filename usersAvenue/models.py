from django.db import models
from django.contrib.auth.models import User
from avenueShop.models import Movies, Genre
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, null=True)
    my_pic = models.ImageField(upload_to='images/' ,null=True, blank=True, default="my-def.jpg")
    email = models.CharField(max_length=200, null=True)
    recidence = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True )

    def __str__(self):
        return self.name

    @property
    def photo_url(self):
        if self.my_pic and hasattr(self.my_pic, 'url'):
            return self.my_pic.url        

class Buy(models.Model):
    buy_type = models.CharField(max_length=100,null=True)
    cost = models.FloatField()

    def __str__(self):
        return self.buy_type 

class Order(models.Model):
    STATUS = (
        ('Incomplete','Incomplete'),
        ('Complete','Complete'),
    )
    
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE) 
    buys_types = models.ForeignKey(Buy, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS, null=True) 
    time_pick = models.TimeField(null=True)
    date_pick = models.DateField(null=True)

