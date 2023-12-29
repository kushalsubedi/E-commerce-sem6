from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=50000)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except Exception:
            url = ''
        return url

    def __str__(self):
        return self.name

    def summary(self):
        return self.body[:300]

    def pub_date_pretty(self):
        return self.created_at.strftime('%b %e %Y')

