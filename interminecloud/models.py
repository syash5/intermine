from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings

#
# Basic Data Points
#
class UserProfile(AbstractUser):

    username = models.CharField('username', max_length=100, unique=True, default="username Should be more than 6 letters,alphanumeric and first letter should be alphabet")
    full_name= models.CharField(max_length=50, default="",blank= False)

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=100)
    password= models.CharField(max_length=150,blank=False, default="")
    email = models.EmailField(unique=True, blank=False)
    contact_no = models.CharField(max_length=100,unique=False, blank=False,default="")
    Address = models.CharField(max_length=100, null=True )

    interminedata = models.CharField(max_length=150)


    USERNAME_FIELD = 'email'  # use email to log in
    REQUIRED_FIELDS = ['username']  # required when user is created

    def __str__(self):
        return str(self.username)
    class Meta:
        db_table = "users"


class IntermineCloud(models.Model):
    interminedata = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    machinestart = models.CharField(max_length=100)
    machinestop = models.CharField(max_length=100)
    machinedelete = models.CharField(max_length=100)