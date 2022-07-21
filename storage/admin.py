from django.contrib import admin

# Register your models here.
from storage.models import Message

admin.site.register(Message)