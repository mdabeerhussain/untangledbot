from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.command()
async def info():
    channel = client.get_channel(841727986351865896)
    await channel.send()

client.run("ODQxNzI1NzIyMTQ1NTg3Mjgw.YJq8Kg.FlkGjHYymiFqDakSXMoePM4oLkQ")