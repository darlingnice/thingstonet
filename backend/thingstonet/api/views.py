from django.http import HttpRequest
from rest_framework.decorators import api_view
from users.models import User
from users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def get_user(request:HttpRequest,id:int):
    """ This view function handles GET requests to retrieve a user by their ID. 
        It uses Django REST Framework to serialize the User model instance. 
        If the user exists, it returns the serialized data with a 200 OK status. 
        If the user does not exist, it returns a 404 Not Found error with a descriptive message.
    """
    try:
        instance = User.objects.get(pk=id)
        serializer = UserSerializer(instance=instance)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return  Response(data={"Error":f"No Record for such user with id : {id}"},status=status.HTTP_404_NOT_FOUND)   
            
  
        

        
