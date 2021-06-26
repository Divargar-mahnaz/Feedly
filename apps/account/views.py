from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response

from core.view_handler import NoAuthAPIView, UserAPIView
from .exceptions import UserNotFound, UserRegisterFailed
from .models import User
from .serializer.user import UserLoginSerializer, UserRegisterSerializer


class UserRegisterAPIView(NoAuthAPIView):
    def post(self, request, *args, **kwargs):
        serialized = UserRegisterSerializer(data=request.data)
        if serialized.is_valid(raise_exception=True):
            User.objects.create_user(**serialized.data)
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            raise UserRegisterFailed


class LoginAPIView(NoAuthAPIView):
    def post(self, request, *args, **kwargs):
        serialized = UserLoginSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        user = authenticate(username=serialized.data['username'], password=serialized.data['password'])
        if not user:
            raise UserNotFound
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })


class LogoutAPIView(UserAPIView):
    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(data={'Response': 'you logout successfully'}, status=status.HTTP_200_OK)
