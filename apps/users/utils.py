from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response

from apps.users.tokens import create_jwt_pair_for_user


def login_user(serializer):
    user = authenticate(
        username=serializer.validated_data["username"],
        password=serializer.validated_data["password"]
    )

    if user is not None:
        tokens = create_jwt_pair_for_user(user)
        response = {"message": "Login Successful", "tokens": tokens}
        return Response(data=response, status=status.HTTP_200_OK)
    else:
        return Response(
            data={"message": "Invalid username or password"},
            status=status.HTTP_401_UNAUTHORIZED
        )