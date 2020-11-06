from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Pasta(models.Model):
    name = models.CharField(max_length=15)
    price = models.IntegerField()
    image = models.ImageField(upload_to='pasta_image')

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pasta = models.ForeignKey(Pasta, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username+' '+self.pasta.name)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pasta = models.ForeignKey(Pasta, on_delete=models.CASCADE)
    review = models.CharField(max_length=250)

    def __str__(self):
        return str(self.user.username + ' ' + self.pasta.name)


