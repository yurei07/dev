import discord
from discord.ext import commands
from config import DISCORD_TOKEN, RCLONE_REMOTE, LOCAL_PATH
from utils.rclone_runner import run_rclone_sync

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Бот запущен как {bot.user}")

@bot.command(name="sync")
async def syns_files(ctx):
    await ctx.send("🔄 Начинаю синхронизацию...")
    result = run_rclone_sync(RCLONE_REMOTE, LOCAL_PATH)
    await ctx.send(result)

bot.run(DISCORD_TOKEN)

