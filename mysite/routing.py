# chat/routing.py
from django.urls import re_path

from chat import consumers as chat_consumer
from automation import consumers as auto_consumer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", chat_consumer.ChatConsumer.as_asgi()),
    re_path(r'ws/automation/$', auto_consumer.AutomationConsumer.as_asgi()),
]