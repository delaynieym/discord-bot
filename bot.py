import discord
import random
emojis = ["😂","👀", "👏", "✔", "😢", "💕", "👍", "🙌", "🤞", "🎁", "🤔", "🤣", "💋", "🎶", "🎉", "😊"]
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message):
        print("message received")
        if (message.channel.id != 530491424529973260) and (message.channel.id != 675993960178647040) and (message.channel.id != 569586147160883241):
            print("not allowed")
            print(message.channel.id)
            return
        print("allowed")
        r = random.randint(1,20)
        if r == 1:
            for em in emojis:
                await message.add_reaction(em)
client = MyClient()
client.run('You\'re token here')
