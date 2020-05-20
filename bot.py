from keyhouse import *
import discord
import random
whitelistChannels = [530491424529973260, 675993960178647040, 569586147160883241]
emojis = ["😂","👀", "👏", "✔", "😢", "💕", "👍", "🙌", "🤞", "🎁", "🤔", "🤣", "💋", "🎶", "🎉", "😊"]
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message):
        print("message received")
        if (message.channel.id not in whitelistChannels):
           print("not allowed")
           print(message.channel.id)
           return
        print("allowed")
        r = random.randint(1,20)
        if r == 1:
            for em in emojis:
                await message.add_reaction(em)
client = MyClient()
client.run(ghostKey)