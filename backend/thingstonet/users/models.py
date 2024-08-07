from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.models import Group
from utilities.models import validate_unique_email


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
        if extra_fields.get("is_staff") is not True:
            raise ValueError("is_staff field must be set to True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("is_superuser field must be set to True")
        if extra_fields.get("is_active") is not True:
            raise ValueError("is_active field must be set to True")
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True, error_messages={
            'unique': "user with this email already exists.",
            'invalid': "Please enter a valid email address.",
            'blank': "The email field cannot be empty.",
            'null': "The email cannot be null.",
        })
    phone = models.CharField(
        max_length=11, 
        unique=True,
        error_messages={
            'unique': "user with this phone already exists.",
            'invalid': "Please enter a valid email address.",
            'blank': "The email field cannot be empty.",
            'null': "The email cannot be null.",
        })                      
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # def save(self, *args, **kwargs):
    #     validate_unique_email(self.email, 'User', 'Developers')
    #     super().save(*args, **kwargs)

    
    def __str__(self):
        return self.email
    
# ROLE_PERMISSIONS = {
#     'project_manager': {'is_staff': True, 'is_superuser': False},
#     'backend_developer': {'is_staff': True, 'is_superuser': False},
#     'frontend_developer': {'is_staff': True, 'is_superuser': False},
#     'embedded_systems_developer': {'is_staff': True, 'is_superuser': False},
#     'devops_engineer': {'is_staff': True, 'is_superuser': False},
#     'qa_engineer': {'is_staff': True, 'is_superuser': False},
#     'security_specialist': {'is_staff': True, 'is_superuser': False},
#     'support_engineer': {'is_staff': True, 'is_superuser': False},
#     'api_integration_developer': {'is_staff': True, 'is_superuser': False},
#     'data_engineer_analyst': {'is_staff': True, 'is_superuser': False},
#     'superuser': {'is_staff': True, 'is_superuser': True},  
# }


# class Role(models.Model):
#     ROLE_CHOICES = [
#         ('project_manager', 'Project Manager'),
#         ('backend_developer', 'Backend Developer'),
#         ('frontend_developer', 'Frontend Developer'),
#         ('embedded_systems_developer', 'Embedded Systems Developer'),
#         ('devops_engineer', 'DevOps Engineer'),
#         ('qa_engineer', 'Quality Assurance Engineer'),
#         ('security_specialist', 'Security Specialist'),
#         ('support_engineer', 'Support Engineer'),
#         ('api_integration_developer', 'API/Integration Developer'),
#         ('data_engineer', 'Data Engineer'),
#     ]

    

#     developer = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=30, choices=ROLE_CHOICES)
#     assigned_date = models.DateTimeField(auto_now_add=True)

  
#     def save(self, *args, **kwargs):
#         # Automatically set the is_staff and is_superuser flags based on the role
        
#         permissions = ROLE_PERMISSIONS.get(self.role, {'is_staff': False, 'is_superuser': False})
#         self.developer.is_staff = permissions['is_staff']
#         self.developer.is_superuser = permissions['is_superuser']
#         self.developer.save()
        
#         super().save(*args, **kwargs)


  
