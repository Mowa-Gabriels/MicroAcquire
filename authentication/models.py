

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager

from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
import random
from django.utils.text import slugify






class User(AbstractBaseUser, PermissionsMixin):

   
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', max_length=30)
    last_name = models.CharField('last name', max_length=30, blank=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField('staff', default=True)
    is_seller = models.BooleanField('seller', default=False)
    is_buyer = models.BooleanField('buyer', default=False)
    is_verified    = models.BooleanField('verified', default=False)
    username = None    




    objects = UserManager()

    USERNAME_FIELD = 'email'
    

    class Meta:
        verbose_name = ('username')
        verbose_name_plural =('users')

    def __str__(self):
        return self.email
    

    def tokens(self):
        refresh = RefreshToken.for_user(self)
         
        return{
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    
    def save(self, *args, **kwargs):
        # Combine last name and random 6 numbers
        random_numbers = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        combined_slug = f"{slugify(self.first_name)}-{random_numbers}"

        # Assign the generated slug to the slug field
        self.slug = combined_slug

        super().save(*args, **kwargs)


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    linkedin_profile = models.URLField(blank=True, null=True)
    twitter_profile = models.URLField(blank=True, null=True)
    facebook_profile = models.URLField(blank=True, null=True)
    phone_no = models.CharField(max_length=14, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.email} -profile'
    
    @property
    def avatarUrl(self):
        try:
            url = self.avatar.url
        except:
            url = ''
        return url

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()