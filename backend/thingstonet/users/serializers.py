from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    """
        UserSerializer is a DRF serializer for the User model. It serializes 
        and deserializes user data, converting it to and from JSON. 

        - The `Meta` class links the serializer to the User model and includes
          'email', 'phone', and 'password'. The 'password' field is write-only.

        - The `create` method hashes the user's password before saving it to
          the database.

        - The `validate_phone` method ensures the phone number contains only 
          digits and is exactly 10 digits long.
    """
    class Meta:
        model = User
        fields = ['email','phone','password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        hashed_password = make_password(validated_data['password'])
        validated_data['password'] = hashed_password
        return  User.objects.create(**validated_data)   
    def validate_phone(self, value:str):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        if len(value) != 11:  
            raise serializers.ValidationError("Phone number must be 11 digits long.")
        return value
