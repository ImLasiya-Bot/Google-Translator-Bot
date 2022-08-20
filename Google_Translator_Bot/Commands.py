import os, asyncio, aiofiles, aiofiles.os, datetime, traceback,random, string, time, logging
logger = logging.getLogger(__name__)
from random import choice
from Google_Translator_Bot.Database import Database
from pyrogram import filters
from pyrogram import Client as google_transletor_bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Google_Translator_Bot.Language import BOT_LANGUAGE, GROUP_LANGUAGE
from translation import Translation
from googletrans import Translator
from config import Config

db = Database()

@google_transletor_bot.on_message(filters.command("tr"))
async def echo(client, message): 
    await message.reply_text(
        Translation.TRANSLATED_MSG,
        reply_markup = GROUP_LANGUAGE,
        quote = True
    )
