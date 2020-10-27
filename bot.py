from config import get_config
import discord
from random import randrange, randint


class Client(discord.Client):

    def __init__(self, config=None):
        discord.Client.__init__(self)
        self.config = config

    def print_guilds(self):
        print("Guilds Connected:")
        for guild_id in self.config["guild_order"]:
            for guild in self.guilds:
                if guild.id == guild_id:
                    print(str(guild.id) + " " + guild.name)

    async def on_ready(self):
        print('Connected as', self.user)
        # self.print_guilds()
        # await self.print_guild_members(759959782022184980)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        # If Jared says something in the CTMUN Social Server, reply a sarcastic comment
        if message.guild.id == 759959782022184980 and message.author.id == 690732698234257408 and randint(0, 1) == 0:
            print("Replying sarcastic message to Jared...")
            await self.send_sarcastic_message(message.channel)

        # If Grayson says something in the Bot Testing Server, reply a sarcastic comment
        if message.guild.id == 760945039328673822 and message.author.id == 175063777048395776:
            print("Replying sarcastic message to Grayson...")
            await self.send_sarcastic_message(message.channel)

        # Just because
        if message.content == 'ping':
            await message.channel.send('pong')


    async def create_invite_links(self):
        for guild_id in self.config["guild_order"]:
            for guild in self.guilds:
                if guild.id == guild_id:
                    for channel in guild.channels:
                        if channel.name == "general" and isinstance(channel, discord.TextChannel):
                            invite = await channel.create_invite()
                            print(invite.url)


    async def send_sarcastic_message(self, channel):
        message = self.config['sarcastic_messages'][randrange(0, len(self.config['sarcastic_messages']))]
        await channel.send(message)


    async def print_guild_members(self, guild_id):
        for guild in self.guilds:
            if guild.id == guild_id:
                async for member in guild.fetch_members():
                    print(str(member.id) + " " + member.display_name)




def main():
    config = get_config()
    token = config['discord_token']
    client = Client(config=config)
    client.run(token)



main()
