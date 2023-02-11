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

@Client.on_message(filters.command("myrating"))
async def myratingsa(c:Client, m:Message):
    sy=0
    metin = """**🏆 Qlobal üzrə Ən yaxşı 20 oyunçu \n**"""
    eklenen = 0
    l=[]
    for i in datam.find():
        try:
            if not i["tür"]=="kanal":
                l.append(i)
        except:
            if not int(i["puan"])==0:
                l.append(i)
    l.sort(reverse = True,key=lambda x: int(x["puan"]))
    for i in l[:20]:
        kisi=i["men"]
        puan=i["puan"]

@Client.on_message(filters.command("rating"))
async def ratingsa(c:Client, m:Message):
    sy=0
    metin = """**🏆 Qlobal üzrə Ən yaxşı 20 oyunçu \n**"""
    eklenen = 0
    l=[]
    for i in datam.find():
        try:
            if not i["tür"]=="kanal":
                l.append(i)
        except:
            if not int(i["puan"])==0:
                l.append(i)
    l.sort(reverse = True,key=lambda x: int(x["puan"]))
    for i in l[:20]:
        kisi=i["men"]
        puan=i["puan"]
        sy+=1
        md=""
        if sy==1:
            md="1)"
        if sy==2:
            md="2)"
        if sy==3:
            md="3)"
        if sy==4:
            md="4)"
        if sy==5:
            md="5)"
        if sy==6:
            md="6)"
        if sy==7:
            md="7)"
        if sy==8:
            md="8)"
        if sy==9:
            md="9)"
        if sy==10:
            md="10)"
        if sy==11:
            md="11)"
        if sy==12:
            md="12)"
        if sy==13:
            md="13)"
        if sy==14:
            md="14)"
        if sy==15:
            md="15)"
        if sy==16:
            md="16)"
        if sy==17:
            md="17)"
        if sy==18:
            md="18)"
        if sy==19:
            md="19)"
        if sy==20:
            md="20)"
        metin += f"\n{md} {kisi}  ➡️   {puan} Xal"
    await c.send_message(m.chat.id, metin)
