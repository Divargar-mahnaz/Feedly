from rest_framework import serializers


class RequestOTPSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
