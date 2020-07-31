from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, nmae, password=None):
        """create a new user profile"""
        if not email:
            raise ValueError("user must have an email address")
        

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    
    def create_superuser(self, email, name, password):
        """create and save new superuser"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """database models for users in the system"""
    email = models.EmailField(unique=True, max_length=254)
    name = models.CharField(max_length=255)

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    
    def get_short_name(self):
        return self.name

    
    def __str__(self):
        """Return String representation of our user"""
        return self.email

