from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    bio = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'confirm_password', 'bio', 'profile_picture')

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords must match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

