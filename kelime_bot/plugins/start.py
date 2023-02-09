from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "➕𝐌ə𝐧𝐢 𝐪𝐫𝐮𝐩𝐚 ə𝐥𝐚𝐯ə 𝐞𝐭➕",
            url="http://t.me/BorzSozGame_bot?startgroup=new",
        )
    ],
    [
        InlineKeyboardButton(" 𝐎𝐰𝐧𝐞𝐫🇦🇿 ", url="t.me/ordayam_5_deqiqeye"),
        InlineKeyboardButton("𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="t.me/my_group130"),
        InlineKeyboardButton("Etiraf Botu", url="t.me/BorzEtirafBot"),
        InlineKeyboardButton("Song Botu", url="t.me/BorzSongBot"),
        InlineKeyboardButton("Etiraflar", url="t.me/BORZEtiraflar"),
    ],
])


START = """
**🔮 Salam, BorzSozGame Söz Bota xoş gəldin bu bot ilə söz tapmaq oyunu oynaya bilərsiniz..**

➤ Məlumat üçün 👉 /help üzərinə klikləyin.  Əmrlər asan və sadədir.
"""

HELP = """
**✌️ Əmrlər menyusuna xoş gəlmisiniz.**


/oyna - Söz tap oyunu başladır.. 
/kec - sözü keçər.
/reytinq - Oyunçular arasında rəqabət məlumatları..
/dayan - söz tap oyununu dayandırar.
"""

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://telegra.ph/file/fbae3dc2b7e5c3863c1d5.jpg",caption=START,reply_markup=keyboard)

@Client.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://telegra.ph/file/fbae3dc2b7e5c3863c1d5.jpg",caption=HELP) 

# Oyunu başlat. 
@Client.on_message(filters.command("oyna"))
async def kelimeoyun(c:Client, m:Message):
  global oyun
  aktif = False
  try:
      aktif = oyun[m.chat.id]["aktif"]
      aktif = True
  except:
      aktif = False

  if aktif:
    await m.reply("**❗ Qrupunuzda  oyun artıq davam edir ✍🏻 \n Oyunu dayandırmaq üçün /dayan yaza bilərsiniz")
  else:
    await m.reply(f"**{m.from_user.mention}** Tərəfindən! \nSöz Tapma Oyunu Başladı .\n\nUğurlar !", reply_markup=kanal)

    oyun[m.chat.id] = {
        "kelime": kelime_sec(),
        "aktif": True,
        "round": 1,
        "kec": 0,
        "oyuncular": {},
    }
    kelime = list(oyun[m.chat.id]['kelime'])
    shuffle(kelime)

    kelime_list = "".join(f"{harf} " for harf in kelime)
    text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/100 
📝 Söz :   <code>{kelime_list}</code>
💰 Qazandığın Xal: 50
🔎 İpucu: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {len(kelime_list) // 2} 

✏️ Qarışıq hərflərdən ibarət sözü tapın 
        """
    await c.send_message(m.chat.id, text)
        
