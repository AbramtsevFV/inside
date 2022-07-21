from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from authentication.models import User
from storage.models import Message
from storage.serializers import MessageSerializer


class MessageView(APIView):
    """ Класс для работы с сообщениями """
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer

    def post(self, request):
        """
         :param request:
             json
             history number - number положительное целое число
         :return:
             Если параметр message содержит history и число записей возвращаем последнее 10.
             иначе сохраняем сообщение в БД
         """
        # Подготовка и проверка данных
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(username=serializer.data['user']).first()
        message = serializer.data['message'].strip()

        if user is None:
            # Если пользователь отсутствует в бд.
            return Response(status=status.HTTP_204_NO_CONTENT, data={'message': 'User not found'})

        if message.startswith('history'):
            # Если записей в бд больше message_limit берём последние 10,
            # иначе берём с первой по последнюю.

            # Получаем необходимое количество сообщений.
            message_limit_lst = message.split()
            if len(message_limit_lst) != 2 or not message_limit_lst[1].isdigit():
                # Проверка что строка пришла именно в виде <history number>
                return Response(status=status.HTTP_204_NO_CONTENT,
                                data={'message': f'Invalid arguments.'})

            message_limit = int(message_limit_lst[1])
            messages = Message.objects.filter(user=user)
            total = messages.count()
            if total > message_limit:
                messages_to_send = messages[total-message_limit:total]

            else:
                messages_to_send = messages[0: message_limit]
            serializer = MessageSerializer(data=messages_to_send, many=True)
            serializer.is_valid()
        else:
            # Сохранение сообщения.
            created = Message.objects.create(user=user, message=message)
            if not created:
                return Response(status=status.HTTP_204_NO_CONTENT,
                                data={'message': f'The message was not created.'})
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
