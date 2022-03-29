from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, first_name, last_name, mobile, password, **extra_fields):
        if not email:
            raise ValueError('Email must be provided')
        if not password:
            raise ValueError('Password must be provided')

        user = self.model(
            email = self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self.db)

    def create_user(self, email, first_name, last_name, mobile, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, first_name, last_name, mobile, password, **extra_fields)

    def create_superuser(self, email, first_name, last_name, mobile, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, first_name, last_name, mobile, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=150, blank=True) 
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True, max_length=200)
    mobile = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Books(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Book_Name = models.CharField(max_length=50)
    Book_Category = models.CharField(max_length=50)
    Book_Author = models.CharField(max_length=50)
    Book_Price = models.FloatField()
    
