import discord
from discord.ext import commands, tasks
import requests
from datetime import datetime
import asyncio
from dotenv import load_dotenv
import os #allows 
import pytz #timezone



load_dotenv() #loads .env file, sets variable token to discord token
token = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default() #sets bot permissions to default
intents.message_content = True #allows bot to read messages
bot = commands.Bot(command_prefix = '!martyr ', intents=intents, help_command=None) #sets up bot commands, prefix is !martyr, disables default help command

EST = pytz.timezone('US/Eastern') #sets time zone
CHANNEL_ID = None #channel ID, scheduled time, and last post date are NONE because these have to be set by user
SCHEDULED_TIME = None
LAST_POST_DATE = None

def get_martyrology(month, day):
    response = requests.get(f"http://api:5000/martyrology/{month}/{day}") #calls API to get the martyrology for the given month and day, 
    if response.status_code == 200:
        data = response.json() #formats the response to make it more readable
        text = data['Martyrology']
        text = text.replace('&mdash;', "—")
        text = text.replace('\n', " ")
        return text
    return "No martyrology found for this date."

@bot.event
async def on_ready(): #shows in console its on
    print(f"Bot is online as {bot.user}")

@bot.command() #tells bot that the function is going to be a command, so function today is !martyr today, etc. with other async func
async def today(ctx):
    global CHANNEL_ID, SCHEDULED_TIME
    today = datetime.now(EST)
    text = get_martyrology(today.month, today.day)
    await ctx.send(text) #await is needed because the bot has to wait for the API response before it can send the message, and it also allows the bot to do other things while waiting for the response, like responding to other commands or messages.
    await ctx.send("\n\nPrecious in the sight of the Lord, is the death of his saints.") 

@bot.command()
async def schedule(ctx, time: str):
    global CHANNEL_ID, SCHEDULED_TIME
    if ":" not in time:
        time = time[:2] + ":" + time[2:]
    if daily_post.is_running(): #since daily_post is a loop, it has to be checked if its running before scheduling a time.
        await ctx.send(f"The Martyrology is scheduled to post daily at {SCHEDULED_TIME}. Use !martyr reschedule to change the time or !martyr unschedule to stop daily posts.")
    else:
        CHANNEL_ID = ctx.channel.id
        SCHEDULED_TIME = time
        await ctx.send(f"Daily Martyrology posts scheduled for {SCHEDULED_TIME}")
        daily_post.start()

@bot.command()
async def date(ctx, time: str): #time (which is the date in this context, as a variable with the same name as a function causes confusion) must be a string for it to be read, and it has to be in the format MM-DD, so it can be split into month and day.
    try:
        month, day = map(int, time.split('-'))
        await ctx.send(f"Here is the martyrology for {month}/{day}\n")
        text = get_martyrology(month, day)
        await ctx.send(text)
        await ctx.send("\n\nPrecious in the sight of the Lord, is the death of his saints.")
    except ValueError:
        await ctx.send("Invalid date format. Please use MM-DD.")

@bot.command()
async def reschedule(ctx, time: str):
    global CHANNEL_ID, SCHEDULED_TIME
    if ":" not in time:
        time = time[:2] + ":" + time[2:]
    if daily_post.is_running():
        daily_post.cancel()
        await asyncio.sleep(2)
    CHANNEL_ID = ctx.channel.id
    SCHEDULED_TIME = time
    await ctx.send(f"Daily Martyrology posts rescheduled for {SCHEDULED_TIME}")
    daily_post.start()

@bot.command()
async def unschedule(ctx):
    global CHANNEL_ID, SCHEDULED_TIME
    if daily_post.is_running():
        daily_post.cancel()
        CHANNEL_ID = None
        SCHEDULED_TIME = None
        await ctx.send("Daily posts have been unscheduled")
    else:
        await ctx.send("No daily post time is scheduled.")

@bot.command()
async def help(ctx):
    help_text = """
**!martyr today** - Get today's martyrology.
**!martyr date MM-DD** - Get martyrology for a specific date.
**!martyr schedule HH:MM** - Schedule daily posts at a specific time (24-hour format).
**!martyr reschedule HH:MM** - Change the scheduled time for daily posts.
**!martyr unschedule** - Stop daily posts.
    """
    await ctx.send(help_text)

@tasks.loop(minutes=1)
async def daily_post():
    global LAST_POST_DATE
    now = datetime.now(EST).strftime("%H:%M")
    today = datetime.now(EST).date()
    if now == SCHEDULED_TIME and LAST_POST_DATE != today: #if current time matches scheduled time AND last post date (for daily) was not today, then post martyrology for today and set last post time to today. 
        LAST_POST_DATE = today
        channel = bot.get_channel(CHANNEL_ID)
        today = datetime.now(EST)
        text = get_martyrology(today.month, today.day)
        await channel.send(f"Here is the martyrology for today, {today.month}/{today.day}:\n")
        await channel.send(text)
        await channel.send("\n\nPrecious in the sight of the Lord, is the death of his saints.")

bot.run(token)