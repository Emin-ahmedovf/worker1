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

@Client.on_message(filters.command("stat") & filters.user(OWNER_ID))
async def kelimeoyun(c:Client, m:Message):
    tt=0
    kn=0
    for us in datam.find():
        tt+=1
    for us in datam.find({"tür":"kanal"}):
        kn+=1
    tt=tt-kn
    await m.reply(f"**〽️ Statistika:\n\nℹ️ Toplam User: {tt}\n♻️ Toplam Guruplar: {kn}**")
