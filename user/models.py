import time
import datetime
from PIL import Image
from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            first_name,
            last_name,
            date_of_birth,
            password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    USER_TYPE = [
        ('STUDENT',_('STUDENT')),
        ('PREMIUM',_('PREMIUM')),
        ('GENERAL',_('GENERAL')),
    ]

    GENDER_TYPE = [
        ('MALE',_('MALE')),
        ('FEMALE',_('FEMALE'))
    ]
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    date_of_birth = models.DateField()
    gender = models.CharField(choices=GENDER_TYPE,default='MALE',max_length=7)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_type = models.CharField(choices=USER_TYPE,max_length=8)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    @property
    def get_full_name(self):
        return self.first_name +' '+ self.last_name
    
    def __str__(self):
        return self.email


def user_directory_path(instance, filename):
    user_name = str(instance)[:-8]
    timestap = int(time.time()*1000)
    _,ext = filename.split('.')
    f_name = user_name + str(timestap)+'.'+ext
    return f'user/{user_name}/{f_name}'

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    avater = models.ImageField(blank=True,null=True,upload_to=user_directory_path)
    cover_photo = models.ImageField(blank=True,null=True,upload_to=user_directory_path)
    user_wallet = models.IntegerField(default=0)
    subscription_ends = models.DateField(default=datetime.date(2023,1,1))
    country = CountryField(blank_label="(select country)",blank=True,null=True)

    @property
    def is_subscribed(self):
        return self.subscription_ends > datetime.date.today()
    
    def save(self,*args, **kwargs):
        try:
            prev = UserProfile.objects.get(user=self.user)
            if prev.cover_photo != self.cover_photo:
                import os
                if os.path.exists(prev.cover_photo.path):
                    print(prev.cover_photo.name)
                    os.remove(prev.cover_photo.path)
            if prev.avater != self.avater:
                import os
                if os.path.exists(prev.avater.path):
                    print(prev.avater.name)
                    os.remove(prev.avater.path)
        except:
            pass
        finally:
            super().save(*args, **kwargs)
            if self.cover_photo:
                c_p = Image.open(self.cover_photo)
                c_p = c_p.resize((744,200))
                c_p.save(self.cover_photo.path)
            if self.avater:
                p_p = Image.open(self.avater)
                p_p = p_p.resize((150,150))
                print('_'*100)
                print(self.avater.path)
                print(p_p)
                p_p.save(self.avater.path)
                print('_'*100)
    
    def __str__(self):
        return self.user.email
    