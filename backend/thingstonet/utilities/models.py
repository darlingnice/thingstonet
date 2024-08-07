# utilities/validators.py
from django.core.exceptions import ValidationError
from django.apps import apps
from django.db import models

def validate_unique_email(email, user_model_name, developer_model_name):
    UserModel = apps.get_model('users', user_model_name) 
    DeveloperModel = apps.get_model('developers', developer_model_name)  

    if UserModel.objects.filter(email=email).exists() or \
       DeveloperModel.objects.filter(email=email).exists():
        raise ValidationError('user with this email already exists.')

def validate_unique_phone(phone, user_model_name, developer_model_name):
    UserModel = apps.get_model('users', user_model_name) 
    DeveloperModel = apps.get_model('developers', developer_model_name)  

    if UserModel.objects.filter(phone=phone).exists() or \
        DeveloperModel.objects.filter(phone=phone).exists():
            raise ValidationError('user with this phone already exists.')
   


