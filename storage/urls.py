from django.urls import path

from storage.views import MessageView

app_name = 'storage'

urlpatterns = [
    path('message/', MessageView.as_view(), name='message'),

]
