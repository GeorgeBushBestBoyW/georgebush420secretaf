import os
import uwuify
import time
import discum
import discord
import random
from discord.ext import commands



width = os.get_terminal_size().columns
client = commands.Bot(command_prefix=".", self_bot=True, help_command=None)
token = ""
client.uwuifyStatus = False
client.respondStatus = False
client.command_prefix = "."


print("██╗░░░██╗░█████╗░░██████╗░█████╗░".center(width), end='')
print("██║░░░██║██╔══██╗██╔════╝██╔══██╗".center(width), end='')
print("╚██╗░██╔╝██║░░██║╚█████╗░███████║".center(width), end='')
print("░╚████╔╝░██║░░██║░╚═══██╗██╔══██║".center(width), end='')
print("░░╚██╔╝░░╚█████╔╝██████╔╝██║░░██║".center(width), end='')
print("░░░╚═╝░░░░╚════╝░╚═════╝░╚═╝░░╚═╝".center(width))

@client.event
async def on_ready():
    print('Logged in as {0}'.format(client.user).center(width))


@client.event
async def on_message(message):
    if (not message.content.startswith('.') or message.content == "" or message.content == None):
        if client.uwuifyStatus == True:
            if message.author.id == 822475574580346931:
                uwuedMsg = uwuify.uwu(message.content)
                await message.edit(content=uwuedMsg)
    await client.process_commands(message)

@client.event
async def on_message(message):
    if message.content.startswith("<@822475574580346931>"):
            if client.respondStatus == False:
                print('! Pinged in',client.get_channel(message.channel.id), 'in', client.get_guild(message.guild.id), 'by', client.get_user(message.author.id))
            else:
                await message.channel.send('vyhul mi')
                print('! Pinged in',client.get_channel(message.channel.id), 'in', client.get_guild(message.guild.id), 'by', client.get_user(message.author.id))
    await client.process_commands(message)

@client.command()
async def test(ctx):
    await ctx.message.delete()
    await ctx.channel.send('Cock')
    print('>> Test command executed')

@client.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.channel.send('```.test - Test command\n.uwuify - Uwuify your message\n.coinflip - Flip a coin\n.autorespond - Respond to any ping with a message```')
    print('>> Help command executed')

@client.command()
async def uwuify(ctx):
    await ctx.message.delete()
    if client.uwuifyStatus == False:
        await ctx.channel.send('`Uwuify enabled`', delete_after=2)
        print('>> Uwuify enabled')
        client.uwuifyStatus = True
    else:
        client.uwuifyStatus = False
        await ctx.channel.send('`Uwuify disabled`', delete_after=2)
        print('>> Uwuify disabled')

@client.command()
async def autorespond(ctx):
    await ctx.message.delete()
    if client.respondStatus == False:
        await ctx.channel.send('`AutoRespond enabled`', delete_after=2)
        print('>> AutoRespond enabled')
        client.respondStatus = True
        print('pico on')
    else:
        client.respondStatus = False
        await ctx.channel.send('`AutoRespond disabled`', delete_after=2)
        print('>> AutoRespond disabled')

@client.command()
async def coinflip(ctx):
    await ctx.message.delete()
    cf = random.randint(1,10)
    if (cf == 1 or cf == 2 or cf == 3 or cf == 4 or cf == 5):
        print('>> You rolled Heads', cf)
        await ctx.channel.send('Flipping...', delete_after=0)
        time.sleep(2)
        await ctx.channel.send('`Heads`', delete_after=4)
    else:
        print('>> You rolled Tails', cf)
        await ctx.channel.send('Flipping...', delete_after=0)
        time.sleep(2)
        await ctx.channel.send('`Tails`', delete_after=4)


client.run(token)
