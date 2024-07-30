from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
 
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get("is_staff") is not True :
            raise ValueError("is_staff field must be set to True")
        if extra_fields.get("is_superuser") is not True :
            raise ValueError("is_superuser field must be set to True")
            
        if extra_fields.get("is_active") is not True :
            raise ValueError("is_active field must be set to True") 
        

        return self.create_user(email, password, **extra_fields)



class User(AbstractBaseUser,PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20,unique=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['phone']

    def __str__(self):
        return self.email




class Organization(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_organizations')
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    

class UserOrganization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'organization')

    def __str__(self):
        return f"{self.user.email} - {self.organization.name}"