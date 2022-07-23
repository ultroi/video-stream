import asyncio

from config import BOT_USERNAME, SUDO_USERS
from program import LOGS
from program.utils.function import get_calls
from driver.queues import QUEUE
from driver.core import user, me_bot
from driver.filters import command, other_filters
from driver.database.dbchat import remove_served_chat
from driver.database.dbqueue import remove_active_chat
from driver.decorators import authorized_users_only, bot_creator, check_blacklist
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.raw.types import InputPeerChannel
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant, ChatAdminRequired


 
@Client.on_message(command(["startvc", f"startvc@{BOT_USERNAME}"]) & filters_ex)
async def start_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    msg = await c.send_message(chat_id, "`starting...`")
    try:
        peer = await user.resolve_peer(chat_id)
        await user.send(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=user.rnd_id() // 9000000000,
            )
        )
        await msg.edit_text("✅ Group call started !")
    except ChatAdminRequired:
        await msg.edit_text(
            "The userbot is not admin in this chat. To start the Group call you must promote the userbot as admin first with permission:\n\n» ❌ manage_video_chats"
        )


@Client.on_message(command(["stopvc", f"stopvc@{BOT_USERNAME}"]) & filters_ex)
async def stop_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    msg = await c.send_message(chat_id, "`stopping...`")
    try:
        if not (
            group_call := (
                await get_calls(m, err_msg="group call not active")
            )
        ):
            await msg.edit_text("❌ The group call already ended")
            return
        await user.send(
            DiscardGroupCall(
                call=group_call
            )
        )
        await msg.edit_text("✅ Group call has ended !")
    except Exception as e:
        if "GROUPCALL_FORBIDDEN" in str(e):
            await msg.edit_text(
                "The userbot is not admin in this chat. To stop the Group call you must promote the userbot as admin first with permission:\n\n» ❌ manage_video_chats"
            )


 
