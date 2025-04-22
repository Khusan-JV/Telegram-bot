from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import asyncio

api_id = 21486721        # замени на свои
api_hash = 'd4866b731c1a2230e6bc9fdbaa0655c2' # замени на свои
phone = '+998339996606'      # твой номер

client = TelegramClient('session', api_id, api_hash)

async def update_name():
    await client.start(phone)
    while True:
        now = datetime.now().strftime('%H:%M')
        await client(UpdateProfileRequest(first_name=f'NEON | {now}'))
        await asyncio.sleep(60)

with client:
    client.loop.run_until_complete(update_name())
  
