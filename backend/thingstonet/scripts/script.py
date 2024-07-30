from users.models import User
from django.contrib.auth.hashers import make_password

def run():
    new_user1 = User(email="uromtudarlington@gmail.com",phone="09024353542",password=make_password('iamaprogrammer2'))
    new_user1.save()






