from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    user = serializers.CharField()
    message = serializers.CharField()
