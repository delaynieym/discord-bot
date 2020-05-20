import discord
import random
emojis = ["😂","👀", "👏", "✔", "😢", "💕", "👍", "🙌", "🤞", "🎁", "🤔", "🤣", "💋", "🎶", "🎉", "😊"]
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message):
        r = random.randint(1,3)
        if r == 1 and not (str(message.author.id) == "207686242874294272"):
            for em in emojis:
                await message.add_reaction(em)
client = MyClient()
client.run('NjkyOTQ4MDMwMDA0OTIwNDEw.XsR9hw.oAWXk_lbC5eRKeSvKXllBgqSwSA')
