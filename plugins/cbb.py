#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"You can use this bot <b>Absolutely Free</b> but this bot want maintenance every month and maintenance cost is too high.🥺\nSo help our creater by paid small amount <b>₹10/month</b> for maintaining this bot server.\n\nIf you want to use this bot then you have to contact our creater.\n\n<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>Royal Krrishna</a>\n○ Channel : @technokrrish\n○ Group : @technokrrishhelp</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
