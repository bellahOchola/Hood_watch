from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Hood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    police_line = models.CharField(max_length=200, blank=True,)
    hood_pic = ImageField(blank=True, manual_crop="")
    hospital_info= models.CharField(max_length=200, blank=True,)

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=700)
    posted = models.DateTimeField(auto_now_add = True)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, null=True)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()



class Profile(models.Model):
    bio = models.TextField(max_length = 500)
    profile_pic = ImageField(blank=True, manual_crop="")
    location = models.CharField(max_length = 100) 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()


class Business(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, help_text='Required. Inform a valid email address.')
    hoodie = models.ForeignKey(Hood, on_delete=models.CASCADE, null=True)
    description= models.TextField(null=True)