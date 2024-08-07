from users.models import User
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.db import IntegrityError

def run():
    ## add new user
    try:
        new_user1 = User(email="jollyboy2@gmail.com",phone="08033490884",password=make_password('iamaprogrammer2'))
        new_user1.is_active = True
        new_user1.save()
    except ValidationError as e:      
        print(e)     
    except IntegrityError as  e:
        print(e)    
    else: 
        print(f"User account saved")    
          








