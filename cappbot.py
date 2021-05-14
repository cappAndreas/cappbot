import discord
import os
import pyjokes
import requests
from chuck import ChuckNorris

cn = ChuckNorris()
data = cn.random()
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Lommetennis'))
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("Yo"):
        await message.channel.send('yo y0')

    if message.content.startswith("!joke"):
        await message.channel.send(pyjokes.get_joke())

    if message.content.startswith("!chuck"):
        await message.channel.send(cn.random().joke)

client.run((TOKEN))
