import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup,CallbackQuery
from info import AUTH_USERS

logger = logging.getLogger(__name__)


@Client.on_message(filters.command('about') & filters.user(AUTH_USERS) if AUTH_USERS else None)
async def about(bot, message):
    """About command handler"""
    buttons = [[
        InlineKeyboardButton('DMCA', callback_data="dmca"),
        InlineKeyboardButton('Need Any Help?', url = "https://t.me/HBMwebgroup"),
    ]]
    reply_markup1 = InlineKeyboardMarkup(buttons)
    await message.reply("**Bot By:-** @HBMweb,@cinema_crave_official & @zeemarathimovies \n\n**Bot:-** @HBMMediaSearch_Robot\n**Developer:-** @EagleScou\n**Updates Channel:-** @HBMweb", reply_markup=reply_markup1)

@Client.on_message(filters.command('help') & filters.user(AUTH_USERS) if AUTH_USERS else None)
async def help(bot, message):
    """Help command handler"""
    await message.reply("""<a href="https://t.me/HBMweb/2969">How To Use Me @HBMMediaSearch_Robot</a>""")

CLOSE = InlineKeyboardMarkup([
            [InlineKeyboardButton(text=' Close ', callback_data="cancel")]
                            ])
@Client.on_callback_query()
async def cb_(client: Client, callback_query: CallbackQuery, retry=False):
  cb_data = callback_query.data
  msg = callback_query.message
  if cb_data == "cancel":
        await msg.delete()
  elif cb_data == "dmca":
        await msg.reply("`All the files in this bot are freely available on the internet or posted by somebody else.This bot is indexing files which are already uploaded on Telegram for ease of searching,We respect all the copyright laws and works in compliance with DMCA and EUCD.If anything is against law please contact us so that it can be removed asap.`",reply_markup = CLOSE)
        await msg.delete()