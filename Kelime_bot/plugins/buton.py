from telethon import Button
from telethon import TelegramClient, events
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
import pymongo
mydb=pymongo.MongoClient("mongodb+srv://emin:emin@cluster0.ny8g8ih.mongodb.net/?retryWrites=true&w=majority")
mydatam=mydb["data1"]
datam=mydatam["soz"]
keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕ Məni Qrupa Əlavə Et ➕", url=f"http://t.me/Goldenoyunbot?startgroup=new")
    ],
    [
        InlineKeyboardButton("🇦🇿  Bot Sahibi ", url="t.me/emin_orjinal"),
        InlineKeyboardButton("🔎 Əmrlər", callback_data ="eme")
    ],
    [
        InlineKeyboardButton("✨ Yeniliklər ✨", url=f"https://t.me/goldenbotresmi")
    ]
])


DOCS_MESSAGE = "• **Salam** 📖\n\n• **Mən Söz Oyun Botuyam** 🎮 \n\n• **Əyləncəli vaxt Keçirmək üçün Mənimlə Oynaya bilərsən** ✍🏻 \n\n• **Oynamaq üçün məni bir qrupa əlavə edib yönetici etmək lazimdir** . 💭"
DOCS_BUTTONS = [
      [
            InlineKeyboardButton("➕ Məni Qrupa Əlavə Et ➕", url=f"http://t.me/Goldenoyunbot?startgroup=new")
    ],
    [
        InlineKeyboardButton("🇦🇿  Bot Sahibi ", url="t.me/emin_orjinal"),
        InlineKeyboardButton("🔎 Əmrlər", callback_data ="eme")
    ],
    [
        InlineKeyboardButton("✨ Yeniliklər ✨", url=f"https://t.me/goldenbotresmi")
    ]
]           


@Client.on_callback_query()
def callback_query(client, CallbackQuery): 
     if CallbackQuery.data == "START READING":
         PAGE1_TEXT = "**Bot Əmrləri Haqqinda** \n\n/game - Yeni oyun başladar\n\n/stop - Oyunu Dayandırar\n\n/rating - Qlobal İstifadəçi Sıralamasini Göstərər\n\n/kec - Bilmədiyiniz Sözü keçər"

         PAGE1_BUTTON = [
               [
                     InlineKeyboardButton("↩️ Geri Qayıt", callback_data="GO TO MENU"),
               ]
         ]

         CallbackQuery.edit_message_text(
             PAGE1_TEXT,
             reply_markup = InlineKeyboardMarkup (PAGE1_BUTTON)
         )         

     elif CallbackQuery.data == "GO TO MENU":
         CallbackQuery.edit_message_text( 
             DOCS_MESSAGE, 
             reply_markup = InlineKeyboardMarkup(DOCS_BUTTONS)
         ) 


@Client.on_message(filters.regex('eme'))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"**Your ID**: `{message.from_user.id}`\n**{reply.from_user.first_name}'s ID**: `{reply.from_user.id}`\n**Chat ID**: `{message.chat.id}`"
        )
    else:
        message.reply(
            f"**Your id**: `{message.from_user.id}`\n**chat id**: `{message.chat.id}`"
        )




START = """
• **Salam** 📖\n\n• **Mən Söz Oyun Botuyam** 🎮 \n\n• **Əyləncəli vaxt Keçirmək üçün Mənimlə Oynaya bilərsən** ✍🏻 \n\n• **Oynamaq üçün məni bir qrupa əlavə edib yönetici etmək lazimdir** . 💭
"""

    
    
    
    
    
    
"""
PRIVATE /start MESSAGE
"""
@Client.on_message(filters.command("start") & filters.private)
async def priv_start(c:Client, m:Message):
    await c.send_message(m.chat.id, START, reply_markup=keyboard)
    try:
        datam.insert_one({"_id":m.chat.id,"puan":"0"})
    except:
        pass
