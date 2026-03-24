import discord
from discord.ext import commands, tasks
import requests
from datetime import datetime
import asyncio
from dotenv import load_dotenv
import os


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '!martyr ', intents=intents)

CHANNEL_ID = None
SCHEDULED_TIME = None
LAST_POST_DATE = None

def get_martyrology(month, day):
    response = requests.get(f"http://api:5000/martyrology/{month}/{day}")
    if response.status_code == 200:
        data = response.json()
        text = data['Martyrology']
        text = text.replace('&mdash;', "—")
        text = text.replace('\n', " ")
        return text
    return "No martyrology found for this date."

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

@bot.command()
async def today(ctx):
    global CHANNEL_ID, SCHEDULED_TIME
    today = datetime.now()
    text = get_martyrology(today.month, today.day)
    await ctx.send(text)
    await ctx.send("Precious in the sight of the Lord, is the death of his saints.")

@bot.command()
async def schedule(ctx, time: str):
    global CHANNEL_ID, SCHEDULED_TIME
    CHANNEL_ID = ctx.channel.id
    SCHEDULED_TIME = time
    await ctx.send(f"Daily Martyrology posts scheduled for {SCHEDULED_TIME}")
    daily_post.start()

@bot.command()
async def date(ctx, time: str):
    try:
        month, day = map(int, time.split('-'))
        await ctx.send(f"Here is the martyrology for {month}/{day}")
        text = get_martyrology(month, day)
        await ctx.send(text)
        await ctx.send("Precious in the sight of the Lord, is the death of his saints.")
    except ValueError:
        await ctx.send("Invalid date format. Please use MM-DD.")

@bot.command()
async def unschedule(ctx):
    global CHANNEL_ID, SCHEDULED_TIME
    if daily_post.is_running():
        daily_post.stop()
        CHANNEL_ID = None
        SCHEDULED_TIME = None
        await ctx.send("Daily posts have been unscheduled")
    else:
        await ctx.send("No daily post time is scheduled.")

@tasks.loop(minutes=1)
async def daily_post():
    global LAST_POST_DATE
    now = datetime.now().strftime("%H:%M")
    today = datetime.now().date()
    if now == SCHEDULED_TIME and LAST_POST_DATE != today:
        LAST_POST_DATE = today
        channel = bot.get_channel(CHANNEL_ID)
        today = datetime.now()
        text = get_martyrology(today.month, today.day)
        await channel.send(text)

bot.run(token)