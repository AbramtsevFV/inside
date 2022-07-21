import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authentication.models import User


class AuthenticationAPITestCase(APITestCase):
    def setUp(self):
        self.data_create_test = json.dumps({
            "username": "fedor",
            "email": "fedor@admn.ru",
            "password": "12345678"})
        self.deta_error_test = json.dumps({
            "username": "",
            "email": "fedor@admn.ru",
            "password": "12345678"})


    def tests_create(self):
        # Проверяем создание пользователя.
        response = self.client.generic('POST', reverse('authentication:user_login'), self.data_create_test,
                                       content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.json()['token']

        # Проверяем, что пользователь возвращается при повторном обращение.
        response = self.client.generic('POST', reverse('authentication:user_login'), self.data_create_test,
                                       content_type="application/json")
        self.assertEqual(response.json()['token'], token)

    def tests_error(self):
        # Проверяем если нет поля
        response = self.client.generic('POST', reverse('authentication:user_login'), self.deta_error_test,
                                       content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"username": ["This field may not be blank."]})



