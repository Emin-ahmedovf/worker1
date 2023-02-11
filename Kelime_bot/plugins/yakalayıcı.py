from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import rating
from kelime_bot.helpers.keyboards import *
from kelime_bot.helpers.kelimeler import kelime_sec
from kelime_bot import *
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
import pymongo
mydb=pymongo.MongoClient("mongodb+srv://emin:emin@cluster0.ny8g8ih.mongodb.net/?retryWrites=true&w=majority")
mydatam=mydb["data1"]
datam=mydatam["soz"]

@Client.on_message(filters.text & ~filters.private)
async def buldu(c:Client, m:Message):
    global oyun
    global rating
    try:
        if m.chat.id in oyun:
            if m.text.lower() == oyun[m.chat.id]["kelime"]:
                await c.send_message(m.chat.id,f"🥳 Təbriklər ! **{m.from_user.mention}** **<code>{oyun[m.chat.id]['kelime']}</code>** , Sözünü Düzgün Tapdı ✅ \n\n Balansınıza 40 xal Əlavə edildi")
                try:
                    datam.insert_one({"_id":m.from_user.id,"puan":"40","men":m.from_user.mention})
                except:
                    r=datam.find_one({"_id":m.from_user.id})
                    u=r
                    u["puan"]=str(int(r["puan"])+40)
                    datam.update_one({"_id":m.from_user.id},{"$set":u})
                try:
                    puan = oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)]
                    oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)] += 40
                except KeyError:
                    oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)] = 40
                
                
                oyun[m.chat.id]["kelime"] = kelime_sec()
                oyun[m.chat.id]["round"] = oyun[m.chat.id]["round"] + 1
                
                if oyun[m.chat.id]["round"] >= 7:
                    siralama = []
                    for i in oyun[m.chat.id]["oyuncular"]:
                        siralama.append(f"{i} :   {oyun[m.chat.id]['oyuncular'][i]}  Xal")
                    siralama.sort(reverse=True)
                    siralama_text = ""
                    for i in siralama:
                        siralama_text += i + "\n"
                    
                    return await c.send_message(m.chat.id, f"✏️ Oyun Bitdi ✓ \n\n📝 Xal qazanan Oyunçuların Siyahısı :\n\n{siralama_text}\n\n• Yeni Oyun Başladmaq üçün /sgame əmrindən istifadə edin!")
                    oyun[m.chat.id] = {}
                
                
                kelime_list = ""
                kelime = list(oyun[m.chat.id]['kelime'])
                shuffle(kelime)
                for harf in kelime:
                    kelime_list+= harf + " "
            
                text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/30 
📝 Söz :   <code>{kelime_list}</code>
💰 Qazandiracağı Xal : 40
🔎 İpucu 1. Hərf : {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {int(len(kelime_list)/2)} 

✏️ Qarişiq Hərflərdən Düzgün Sözü Tap 🥳 
                        """
                await c.send_message(m.chat.id, text)
    except KeyError:
        pass
    
    
gonderilmedi = True
data_message = None
EKLENEN_CHATS = []
@Client.on_message()
async def data(c:Client, m:Message):
    global EKLENEN_CHATS
    global gonderilmedi
    global data_message
    
    chat_id = str(m.chat.id)
    
    if chat_id in EKLENEN_CHATS:
        return

    if gonderilmedi:
        data_message= await c.send_message(OWNER_ID, f"{OWNER_ID}")
        gonderilmedi = False
        
    
    else:
        chats = await c.get_messages(OWNER_ID, data_message.message_id)
        chats = chats.text.split()
        
        if chat_id in chats:
            pass
        else:
            chats.append(chat_id)
            EKLENEN_CHATS.append(chat_id)
            data_text = ""
            for i in chats:
                data_text += i + " "
            await c.edit_message_text(OWNER_ID, data_message.message_id, data_text)
            
            
