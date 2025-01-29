from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    reg_date = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    user_status = models.CharField(max_length=20, default='Active')  # Active, Inactive

    def __str__(self):
        return self.username
