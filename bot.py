from config import get_config
import discord


class Client(discord.Client):

    async def on_ready(self):
        print('Connected as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')


def get_token():
    return get_config()['discord_token']


def main():
    token = get_token()
    client = Client()
    client.run(token)


main()
