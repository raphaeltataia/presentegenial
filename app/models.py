from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

# Create your models here.


class Campaign(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Profile')
    product = models.ForeignKey('Product')
    tag = models.ManyToManyField('Tag')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=False, null=False)

    def ending(self):
        self.end_date = (timezone.now() + datetime.timedelta(30)).isoformat()

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.name


class Product(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Donation(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    campaign = models.ForeignKey('Campaign')
    user = models.ForeignKey('Profile')
    created_date = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.price


class Tag(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)

    def __str__(self):
        return self.price
