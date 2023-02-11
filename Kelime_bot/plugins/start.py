from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
import pymongo
mydb=pymongo.MongoClient("mongodb+srv://emin:emin@cluster0.ny8g8ih.mongodb.net/?retryWrites=true&w=majority")
mydatam=mydb["data1"]
datam=mydatam["soz"]

@Client.on_message(filters.command("sgame") & ~filters.private & ~filters.channel & ~filters.edited)
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        if int(oyun[m.chat.id]["round"]) >= 10:
            oyun[m.chat.id] = {}
        else:
            await m.reply("• Hal-hazırda Davam Edən Oyun Var :)) ✍🏻 \n• Oyunu dayandırmaq üçün /stop əmrindən istifadə edin ✓")

    except:
        oyun[m.chat.id] = {}
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        pass
    else:
        try:
            datam.insert_one({"_id":m.chat.id,"tür":"kanal"})
        except:
            pass
        await m.reply(f"**{m.from_user.mention}** Tərəfindən Söz Oyunu Başladı .\n\n🥳 Xoş Oyunlar....", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["pass"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/30 
📝 Söz :   <code>{kelime_list}</code>
💰 Qazandiracağı Xal : 40
🔎 İpucu : 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {int(len(kelime_list)/2)} 

✏️ Qarişiq Hərflərdən Düzgün Sözü tap 🥳 
        """
        await c.send_message(m.chat.id, text)
        
