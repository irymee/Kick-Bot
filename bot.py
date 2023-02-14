import os
import pymongo
from pymongo import MongoClient
from pyrogram import Client, filters
from pyrogram.types import Message

# Connect to MongoDB
mongo_url = os.environ.get("MONGO_URL")
mongo_client = MongoClient(mongo_url)
db = mongo_client["mydatabase"]
col = db["mycollection"]

# Initialize Pyrogram client
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define command for setting the kick time
@bot.on_message(filters.command("settime") & filters.private)
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

# Define function for kicking members
async def kick_member(chat_id, user_id):
    await app.kick_chat_member(chat_id, user_id)

# Define handler for new members joining a chat
@bot.on_chat_member_updated()
async def on_chat_member_updated(_, update):
    chat_id = update.chat.id
    user_id = update.new_chat_member.user.id
    # Get the kick time from the database
    kick_time = col.find_one({"_id": "kick_time"})
    if kick_time:
        kick_time = kick_time["time"]
    else:
        kick_time = 60 # default kick time is 60 seconds
    # Schedule the member to be kicked after the specified time
    app.scheduler.enqueue_in(kick_time, kick_member, chat_id, user_id)

# Start the bot
app.run()
