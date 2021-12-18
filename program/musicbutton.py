from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import version
from driver.veez import user
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import version as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

major = 0
minor = 2
micro = 1

python_version = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ Welcome {message.from_user.mention()} !\n
💭 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) Allows you to play music and video on groups through the new Telegram's video chats!

💡 Find out all the Bot's commands and how they work by clicking on the » 📚 Commands button!

🔖 To know how to use this bot, please click on the » ❓ Basic Guide button!
""",
        reply_markup=InlineKeyboardMarkup(
            [
 
                [InlineKeyboardButton("❓ Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Commands", callback_data="cbcmds"),
 
        disable_web_page_preview=True,
    )


 

   
     