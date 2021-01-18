import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith("$stress"):
        await msg.channel.send("i am dying inside")
    elif msg.content.startswith("Faith James"):
        await msg.channel.send(" how did you know my creator")
    elif msg.content.startswith("$commands"):
        await msg.channel.send("$stress\n$help\n")
    elif msg.content.startswith("Fuck"):
        await msg.channel.send("nawaoo wetin the work you")
    elif msg.content.startswith("$help"):
        await msg.channel.send("welcome to noob for noobs , contact ahmed the nim dev")
    elif msg.content.startswith("$nim"):
        await msg.channel.send("linux is trash, nim is POWAAA")
    elif msg.content.startswith("brb"):
        await msg.channel.send("ahmed why this na")

client.run(os.environ.get("NIMBOT_TOKEN"))

