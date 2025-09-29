from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.core.call import Anony
from AnonXMusic.utils.database import get_assistant

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await Anony.stop_stream_force(message.chat.id)

@app.on_message(filters.left_chat_member, group=69)
async def bot_kick(_, msg: Message):
    if msg.left_chat_member.id == app.id:
        ub = await get_assistant(msg.chat.id)
        try:
            await ub.leave_chat(msg.chat.id)
        except:
            pass
