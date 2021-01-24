
import dimscord, asyncdispatch, times, options, os

let discord = newDiscordClient(getEnv("NIMBOT_TOKEN"))

# Handle event for on_ready.
proc onReady(s: Shard, r: Ready) {.event(discord).} =
    echo "Ready as " & $r.user

# Handle event for message_create.
proc messageCreate(s: Shard, m: Message) {.event(discord).} =
    if m.author.bot: return
    if m.content == "!help": # If message content is "!ping".
        discard await discord.api.sendMessage(
            m.channel_id,
            embed = some Embed(
                title: some "Hello There",
                description: some  "welcome to noobs for noobs",
                color: some 0x7789ec
                )   
         )   
    elif m.content == "!embed": # Otherwise if message content is "!embed".
        # Sends a message with embed.
        discard await discord.api.sendMessage(
            m.channel_id,
            embed = some Embed(
                title: some "Hello there!", 
                description: some "This is description",
                color: some 0x7789ec
            )
        )

# Connect to Discord and run the bot.
waitFor discord.startSession()
