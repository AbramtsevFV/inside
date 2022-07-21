from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField( max_length=255)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

