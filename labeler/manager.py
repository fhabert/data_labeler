from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, interests, password=None):
       if not email:
           raise ValueError('Email must be provided')
 
       user = self.model(first_name=first_name, last_name=last_name, \
                         email=self.normalize_email(email), interests=interests)
       user.set_password(password)
       user.save(using=self._db)
       return user