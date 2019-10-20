from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserOtherInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    # Add any additional attributes you want
    name      = models.CharField(max_length=50)
    zipcode   = models.IntegerField()
    address   = models.CharField(max_length=100)
    telephone = models.IntegerField()
    admin     = models.IntegerField()
    
    def __str__(self):
        # Build-in attribute of django.contrib.auth.models.User !
        return self.user.username
