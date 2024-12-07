from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    InputMediaPhoto,
    InputMediaVideo,
)
from PURVIMUSIC import app
from config import BANNED_USERS
from PURVIMUSIC.utils.decorators.language import language, languageCB
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@app.on_callback_query(filters.regex("repo") & ~BANNED_USERS)
@languageCB
async def gib_repo(client, CallbackQuery, _):
    await CallbackQuery.edit_message_media(
        InputMediaVideo("https://telegra.ph/file/136b8c8380fb100ab3efa.mp4"),
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data=f"settingsback_helper")]]
        ),
    )
