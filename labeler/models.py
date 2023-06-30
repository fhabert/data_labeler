from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser

class Person(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True, default="fake")
    email = models.EmailField(max_length=30, unique=True)
    first_connexion = models.BooleanField(default=True)
    total_answers = models.IntegerField(default=0)
    good_answers = models.IntegerField(default=0)
    rate_success = models.IntegerField(default=0)
    likes_law = models.BooleanField(default=False,blank=True)
    likes_real_estate = models.BooleanField(default=False, blank=True)
    likes_computer_vision = models.BooleanField(default=False, blank=True)
    password = models.CharField(max_length=20, default=None)
    last_login = models.DateTimeField(null=True, blank=True)

    # USERNAME_FIELD = "email"
    def save(self,*args,**kwargs):
        likes_fields = ["likes_law", "likes_real_estate", "likes_computer_vision"]
        if self.total_answers != 0:
            self.rate_success = int(self.good_answers / self.total_answers * 100)
        else:
            self.rate_success = 0

        super().save(*args, **kwargs)

        # for field in likes_fields:
        #     if getattr(self, field) and field != kwargs.get("update_field"):
        #         setattr(self, field, False)

        # super().save(update_fields=likes_fields)
        


    def __str__(self):
        return self.email
