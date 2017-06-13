# bring in the magic
from django.contrib.auth.models import User
from django.shortcuts import render
from django.db import models
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    """
    purpose: Creates Profile table within database
    args: models.Model: (NA): models class given by Django
    returns: (None): N/A
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    closet_name = models.TextField(blank=False, null=False, max_length=200)

    def __str__(self):  # __unicode__ on Python 2
        return self.user.first_name

    # listen for changes on user. update post-save
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    # listen for changes on user. update post-save
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save() 

    
class Category(models.Model):
    """
    purpose: Creates Category table within database
        Example useage:
    args: models.Model: (NA): models class given by Django
    returns: (None): N/A
    """
    category_name = models.TextField(blank=False, null=False, max_length=200)

    def __str__(self):  # __unicode__ on Python 2
        return self.category_name     
    
    def get_items(self):
        print(dir(self))
        return Item.objects.filter(item_category=self)

class Item(models.Model):
    """
    purpose: Creates Item table within database
    args: models.Model: (NA): models class given by Django
    returns: (None): N/A
    """
    item_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    # django will display a dropdown with these choices
    CATEGORY_CHOICES = (
        ('outerwear', 'OUTERWEAR'),
        ('tops', 'TOPS'),
        ('bottoms', 'BOTTOMS'),
        ('dresses', 'DRESSES'),
        ('shoes', 'SHOES'),
        ('bags', 'BAGS'),
        ('accessories', 'ACCESSORIES'),
        ('jewelry', 'JEWELRY'))

    item_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        choices=CATEGORY_CHOICES)

    description = models.TextField(max_length=500)
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=255)
    image_path = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.title        



                 
