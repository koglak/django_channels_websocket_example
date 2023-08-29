from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .tasks import MyFunc

class AutomationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("automation started...")
        await self.accept()
        await MyFunc(self)

    async def disconnect(self, close_code):
        pass

    async def send_alert(self, message):
        print(message)
        await self.send(text_data=json.dumps({"message": message}))