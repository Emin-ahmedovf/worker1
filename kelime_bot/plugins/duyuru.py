from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from time import sleep
from kelime_bot.plugins.yakalayıcı import data_message
from kelime_bot import OWNER_ID

@Client.on_message(filters.command(["duyuru"], [".", "/"]) & filters.user(OWNER_ID))
async def duyuru(c:Client, m:Message):
    chats = await c.get_messages(OWNER_ID, data_message.message.message_id)
    chats_list = chats.text.split()


    #----> Mesaj içeriği <----
    mesaj = ""
    mesaj = m.text[8:] if m.reply_to_message is None else m.reply_to_message.text
    await c.send_message(m.chat.id,f"**Gönerilecek Grup Sayısı:  {len(chats_list)}\nMesajınız:**\n\n__{mesaj}__")



    #----> Gönderme İşlemi <----
    bas =await c.send_message(m.chat.id, "**Duyuru Yapılmaya Başladı.**")
    for chat in chats_list:
        try:
            await c.send_message(chat, mesaj, disable_web_page_preview=True)
            await bas.edit(f"**Duyuru Yapılmaya Başladı.**\n\nGönderildi: {chat}")
        except:
            pass
        sleep(2)
    await c.send_message(m.chat.id, "**Duyuru İşlemi Bitti Tüm Gruplara Duyurunuz Yollandı.**")
    
    
    
    

@Client.on_message(filters.command(["fduyuru"], [".", "/"]) & filters.user(OWNER_ID))
async def fduyuru(c:Client, m:Message):
    chats = await c.get_messages(OWNER_ID, data_message.message_id)
    chats_list = chats.text.split()


    if m.reply_to_message is None:
        return m.reply("**Mesajı yönlendirme şeklinde duyuru yapmak için yanıtlayın !!**")
    message_id = m.reply_to_message.message_id
    mesaj = f"t.me/{str(m.chat.username)}/{str(message_id)}"
    await c.send_message(m.chat.id,f"**Gönerilecek Grup Sayısı:  {len(chats_list)}\nMesajınız: [Tıkla]({mesaj})**", disable_web_page_preview=True)


    #----> Gönderme İşlemi <----
    bas = await c.send_message(m.chat.id, "**Duyuru Yapılmaya Başladı.**")
    for chat in chats_list:
        try:
            await c.forward_messages(chat,m.chat.id, message_id)
            await bas.edit(f"**Duyuru Yapılmaya Başladı.**\n\nGönderildi: {chat}")
        except:
            pass
        sleep(2)
    await c.send_message(m.chat.id, "**Duyuru İşlemi Bitti Tüm Gruplara Duyurunuz Yollandı.**")
