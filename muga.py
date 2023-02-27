# This example requires the 'message_content' intent.

import discord
from os import getenv
from dotenv import load_dotenv
from Shell import MugaShell

if __name__ == "__main__":
    load_dotenv()

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith(getenv('PREFIX')):
            cmd = message.content.replace(f"{getenv('PREFIX')} ", "")
            shell = MugaShell()
            resp = shell.process_cmd(cmd)
            await message.channel.send(resp)

    client.run(getenv('DISCORD_TOKEN'))


