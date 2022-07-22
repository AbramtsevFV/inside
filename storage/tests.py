import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authentication.models import User


class StorageAPITestCase(APITestCase):
    """ Проверяем создание записей в бд и возврат их пользователю"""

    def setUp(self):
        self.data_unload_test = json.dumps({
            "user": "Olga",
            "message": "тестовые"})

        self.data_get_test = json.dumps({
            "user": "Olga",
            "message": "history 3"})

    def test_unload_message(self):
        user, _ = User.objects.get_or_create(username='Olga', email='olga@mail.ru', password='12345678')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer_{user.token}')

        response = self.client.generic("POST", reverse('storage:message'), self.data_unload_test,
                                    content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(reverse('storage:message'), self.data_unload_test,
                                    content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(reverse('storage:message'), self.data_unload_test,
                                    content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(reverse('storage:message'), self.data_unload_test,
                                    content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(reverse('storage:message'), self.data_get_test,
                                   content_type="application/json")
        self.assertEqual(len(response.json()), 3)
        print(len(response.json()))





