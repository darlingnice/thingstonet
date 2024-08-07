from django.http import HttpRequest
from django.views.decorators.csrf import csrf_protect 
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError


from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import obtain_auth_token


from users.models import User
from users.models import User

from users.serializers import UserSerializer,StaffUserSerializer,AdminUserSerializer,DeveloperStaffSerializer
from users.serializers import UserSerializer


from django.contrib.auth import authenticate, login,logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.middleware.csrf import get_token



# for users
@api_view(['GET'])
def get_user(request:HttpRequest,id):
    """ This view function handles GET requests to retrieve a user by their ID. 
        It uses Django REST Framework to serialize the User model instance. 
        If the user exists, it returns the serialized data with a 200 OK status. 
        If the user does not exist, it returns a 404 Not Found error with a descriptive message.
    """
    try:
        instance = User.objects.get(pk=id)
        
    except User.DoesNotExist:
        return  Response(data={"error":f"No Record for such user with id : {id}"},status=status.HTTP_404_NOT_FOUND)   
            
    else:
        if instance.is_superuser:
            serializer = AdminUserSerializer(instance=instance)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        elif instance.is_staff:
            pass
            serializer =  StaffUserSerializer(instance=instance)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            serializer =  UserSerializer(instance=instance)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
# for users
@login_required(login_url='/api/login')
@api_view(['GET'])      
def get_users(request):
    try:
        instance = User.objects.all()
        
    except User.DoesNotExist:
        return  Response(data={"error":"error occured"},status=status.HTTP_404_NOT_FOUND)   
    else:
        serializer = UserSerializer(instance=instance,many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK) 

@api_view(['POST'])
# @csrf_protect
def add_user(request):
    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.is_staff = True
            serializer.save()
            return Response(data={"message":"User created successfuly"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except ValidationError as e:    
        return Response(e,status=status.HTTP_400_BAD_REQUEST)   


@api_view(['POST'])
# @csrf_protect
def add_staff_user(request):
    try:
        serializer = StaffUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message":"User created successfuly"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except ValidationError as e:    
        return Response(e,status=status.HTTP_400_BAD_REQUEST)   


@api_view(['POST'])
# @csrf_protect
def add_developer(request:HttpRequest):
    try:
        serializer = DeveloperStaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message":"Developer created successfuly"},status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except ValidationError as e:    
        return Response(e,status=status.HTTP_400_BAD_REQUEST) 
@csrf_protect  
@api_view(['POST'])
def login_view(request:Request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)

    if user is not None:
        login(request, user)
        # Get the session key
        # session_key = request.session.session_key
        
        # # Generate the CSRF token
        # csrf_token = get_token(request)
        # print(csrf_token)
        
        return Response(
            {
        'detail': 'Logged in successfully'        
        },
             status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
# @csrf_protect  
@api_view(http_method_names=['GET'])
def logout_view(request:HttpRequest):
    # Log out the user by terminating the session
    logout(request)
    return Response({'detail': 'Logged out successfully'}, status=status.HTTP_200_OK)

# @login_required(login_url='/api/login')
@api_view(["POST"])
# @csrf_protect
def test(request:Response):
    return Response(data=request.data,status=status.HTTP_200_OK)