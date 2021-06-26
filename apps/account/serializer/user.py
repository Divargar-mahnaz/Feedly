from rest_framework import serializers

from ..models import User


class UserLoginSerializer(serializers.Serializer):
    username = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, max_length=20)


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'age')
        extra_kwargs = {
            'password': {'write_only': True}
        }
