from rest_framework import serializers
from rest_framework.authtoken.models import Token

from apps.users.models import CustomUser, Profile
from apps.users.validators import validate_password


class SignUpSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        return validate_password(value)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.get_or_create(user=user)
        return user

    class Meta:
        model = CustomUser
        fields = ['image', 'username', 'nickname', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'refresh_token', 'access_token']
        extra_kwargs = {'username': {'write_only': True},
                        'password': {'write_only': True},
                        'refresh_token': {'read_only': True},
                        'access_token': {'read_only': True}}


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Profile
        fields = ['id', 'user', 'username', 'nickname', 'image']
        read_only_fields = ['user']
