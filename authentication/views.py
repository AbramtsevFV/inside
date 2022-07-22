from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import LoginSerializer

from .renderers import UserJSONRenderer


class LoginAPIView(APIView):
    """ Проверяем наличие пользователя, если нет создаём,  случаях возвращаем токен
     есть возвращаем token"""
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        """
        request: json - с данными пользователя
        response: json - с токеном
        """
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        user, _ = User.objects.get_or_create(**serializer.data)
        return Response(data={'token': user.token}, status=status.HTTP_200_OK)