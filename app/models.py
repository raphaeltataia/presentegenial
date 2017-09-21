from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.template.defaultfilters import slugify

# Create your models here.


class Campaign(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('app.User', related_name='campaigns', on_delete=models.CASCADE)
    product = models.ForeignKey('Product')
    tag = models.ManyToManyField('Tag')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.title


class User(AbstractUser):
    location = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30)
    birthday = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Product(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    created_date = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Donation(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    campaign = models.ForeignKey('Campaign')
    user = models.ForeignKey('app.User', related_name='donations', on_delete=models.CASCADE)
    created_date = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.price


class Tag(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
