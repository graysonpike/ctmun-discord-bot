from config import get_config
import discord


class Client(discord.Client):

    def print_guilds(self):
        print("Guilds Connected:")
        for guild in self.guilds:
            print(guild.name)

    async def on_ready(self):
        print('Connected as', self.user)
        self.print_guilds()

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            print("Guild ID:")
            print(message.guild.id)
            await message.channel.send('pong')


def get_token():
    return get_config()['discord_token']


def main():
    token = get_token()
    client = Client()
    client.run(token)



main()
