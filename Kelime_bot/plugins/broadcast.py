from kelime_bot import OWNER_ID
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
import pymongo
mydb=pymongo.MongoClient("mongodb+srv://emin:emin@cluster0.ny8g8ih.mongodb.net/?retryWrites=true&w=majority")
mydatam=mydb["data1"]
datam=mydatam["soz"]

@Client.on_message(filters.command("broadcast") & filters.reply & filters.user(OWNER_ID))
async def kelimeoyun(c:Client, m:Message):
    tpm1=0
    tpm2=0
    for us in datam.find():
        try:
            if not us["tür"]=="kanal":
                rr=m.reply_to_message
                try:
                    await c.send_message(int(us["_id"]),rr["text"])
                    tpm1+=1
                except:
                    pass
        except:
            rr=m.reply_to_message
            try:
                await c.send_message(int(us["_id"]),rr["text"])
                tpm1+=1
            except:
                    pass
    await m.reply(f"{tpm1} Sayda Usere Gönderildi!")
    for us in datam.find({"tür":"kanal"}):
        rr=m.reply_to_message
        try:
            await c.send_message(int(us["_id"]),rr["text"])
            tpm2+=1
        except:
            pass
    await m.reply(f"{tpm2} Sayda Guruba Gönderildi!")
