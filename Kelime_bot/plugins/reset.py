from pyrogram import Client
from pyrogram import filters
from kelime_bot import OWNER_ID
from pyrogram.types import Message
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
import pymongo
mydb=pymongo.MongoClient("mongodb+srv://emin:emin@cluster0.ny8g8ih.mongodb.net/?retryWrites=true&w=majority")
mydatam=mydb["data1"]
datam=mydatam["soz"]

@Client.on_message(filters.command("reset") & filters.user(OWNER_ID))
async def ratingsa(c:Client, m:Message):
    for us in datam.find():
        try:
            if not us["tür"]=="kanal":
                datam.update_one(us,{"$set":{"puan":"0"}})
        except:
            datam.update_one(us,{"$set":{"puan":"0"}})
    await m.reply("Tüm Puanlar Sıfırlandı")
