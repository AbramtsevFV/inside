from django.db import models

# Create your models here.
from authentication.models import User


class Message(models.Model):
    """ Модель для хранения сообщений"""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    message = models.TextField()

    def __str__(self):
        """ Строковое представление модели """
        return self.user.email
