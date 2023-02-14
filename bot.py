import os
import pymongo
from pymongo import MongoClient
from pyrogram import Client, filters
from pyrogram.types import Message
import aiohttp
from aiohttp import web

# Connect to MongoDB
mongo_url = os.environ.get("MONGO_URL")
mongo_client = MongoClient(mongo_url)
db = mongo_client["mydatabase"]
col = db["mycollection"]

# Initialize Pyrogram client
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")
bot = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Initialize aiohttp web app
async def hello(request):
    return web.Response(text="Hello, world!")

web_app = web.Application()
web_app.add_routes([web.get('/hello', hello)])

# Define filter for group admins
def is_admin(_, __, update):
    chat_id = update.chat.id
    user_id = update.from_user.id
    member = app.get_chat_member(chat_id, user_id)
    return member.status in ("creator", "administrator")

# Define command for setting the kick time
@Client.on_message(filters.command("settime") & filters.private & is_admin)
async def set_time(_, message: Message):
    try:
        # Parse the time from the message text
        time = int(message.text.split()[1])
        # Store the time in the database
        col.update_one({"_id": "kick_time"}, {"$set": {"time": time}}, upsert=True)
        # Send a confirmation message
        await message.reply_text(f"Kick time set to {time} seconds.")
    except:
        # Handle any errors that occur
        await message.reply_text("Error: Invalid command syntax.")

# Set default kick time to 30 days (2592000 seconds)
col.update_one({"_id": "kick_time"}, {"$set": {"time": 2592000}}, upsert=True)

# Define command for adding members to the whitelist
@Client.on_message(filters.command("addtowhitelist") & filters.private & is_admin)
async def add_to_whitelist(_, message: Message):
    try:
        # Parse the user ID from the message text
        user_id = int(message.text.split()[1])
        # Store the user ID in the database
        col.update_one({"_id": "whitelist"}, {"$addToSet": {"user_ids": user_id}}, upsert=True)
        # Send a confirmation message
        await message.reply_text(f"User {user_id} added to whitelist.")
    except:
        # Handle any errors that occur
        await message.reply_text("Error: Invalid command syntax.")

# Define function for kicking members
async def kick_member(chat_id, user_id):
    # Check if the user is whitelisted
    whitelist = col.find_one({"_id": "whitelist"})
    if whitelist and user_id in whitelist["user_ids"]:
        return # Do not kick whitelisted members
    await app.kick_chat_member(chat_id, user_id)

# Define handler for new members joining a chat
@Client.on_chat_member_updated()
async def on_chat_member_updated(_, update):
    chat_id = update.chat.id
    user_id = update.new_chat_member.user.id
    # Get the kick time from the database
    kick_time = col.find_one({"_id": "kick_time"})
    if kick_time:
        kick_time = kick_time["time"]
    else:
        kick_time = 2592000 # default kick time is 30 days (2592000 seconds)
    # Schedule the member to be kicked after the specified time
    app.scheduler.enqueue_in(kick_time, kick_member, chat_id, user_id)

# Start the bot
bot.run()
