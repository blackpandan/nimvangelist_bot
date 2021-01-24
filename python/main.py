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

    profanity = ["fuck", "wtf", "waka", "ubanka", "ewu", "your mother", "your father"]

    par = msg.content
    broken = par.split(" ")

    for i in broken:
        for prof in profanity:
            if i.lower() == prof:
                await msg.channel.send("use of this word is not advisable")
                break

    if msg.content.startswith("$stress"):
        await msg.channel.send("i am dying inside")
    elif msg.content.startswith("Faith James"):
        await msg.channel.send(" how did you know my creator")
    elif msg.content.startswith("$commands"):
        await msg.channel.send("$stress\n$help\n")
    elif msg.content.startswith("Fuck"):
        await msg.channel.send("nawaoo wetin the work you")
    elif msg.content.startswith("$help"):
        await msg.channel.send("welcome to noob for noobs,\nyou can visit https://nim-lang.org\n \n contact ahmed the nim dev for more info\n")
    elif msg.content.startswith("$nim"):
        await msg.channel.send("linux is trash, nim is POWAAA")
    elif msg.content.startswith("brb"):
        await msg.channel.send("ahmed why this na")
    elif msg.content.startswith("sammy") or msg.content.startswith("sam p"):
        await msg.channel.send("anywhere you see am bill am")

    elif msg.content.startswith("test"):
        await msg.channel.send(broken)

    elif msg.content.startswith("$pres"):
        v = msg.content
        val = v.split(" ")
        val.pop(0)
        game = " ".join(val)
        await client.change_presence(activity=discord.Game(name=game))
        await msg.channel.send(f"presence sucessfully changed, game added\n ```{game}```")

@client.event
async def on_member_join(member):
    await msg.channel.send(f"Hello {member} welcome to noobs for noobs")

client.run(os.environ.get("NIMBOT_TOKEN"))

