from telethon.tl.types import ChannelParticipantsAdmins
from telethon import TelegramClient, events
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import pyrogram
from datetime import datetime
from Config import Config
import shutil, psutil, traceback, os
LANGAUGE = os.environ.get("LANGAUGE", "TR")
LOG_CHANNEL = -1001510168247 
BOT_USERNAME = "sozitapbot"


@Client.on_message(filters.command("stats"))
async def botstats(bot: Client, message: Message):
    g4rip = await bot.send_message(message.chat.id, LAN.STATS_STARTED.format(message.from_user.mention))
    all_users = await db.get_all_users()
    groups = 0
    pms = 0
    async for user in all_users:
        if str(user["id"]).startswith("-"):
            groups += 1
        else:
            pms += 1
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    total_users = await db.total_users_count()
    await g4rip.edit(text=LAN.STATS.format(BOT_USERNAME, total_users, groups, pms, total, used, disk_usage, free, cpu_usage, ram_usage, __version__), parse_mode="md")











@Client.on_message(filters.command("start"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await client.send_message(-1001510168247, f"ℹ️ **Yeni Kullanıcı -** {ad}")
     return await event.reply(f"**Merhaba \nGrubunuzdakı Üyeleri Etiketleye Bilirim\nKomutlar için Komutlar Düğmesine Tıklaya Bilirsiz**", buttons=(
                      [
                       Button.inline("Komutlar", data="komutlar")
                      ],
                      [
                       Button.url('Beni Grubuna Ekle', 'https://t.me/StartaggerBot?startgroup=a'),
                       Button.url('Kanal', 'https://t.me/StarBotKanal')
                      ],
                      [
                       Button.url('Sahibim', 'https://t.me/Hayiboo')
                      ],
                    ),
                    link_preview=False)


  if event.is_group:
    return await client.send_message(event.chat_id, f"**Beni Grubuna Aldığın için Teşekkürler ✨**")



@Client.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(Config.BOT_ID):
            await msg.reply(
                f'''`Hey` {msg.from_user.mention} `məni` {msg.chat.title} `qrupuna əlavə etdiyin üçün Təşəkkürlər⚡️`\n\n**Mən Söz Oyun Botuyam 🎮 • Əyləncəli vaxt Keçirmək üçün Mənimlə Oynaya bilərsən ✍🏻 ✨**''')

        elif str(new_user.id) == str(Config.OWNER_ID):
            await msg.reply(
                f'''{msg.from_user.mention} Sahibim İndicə Qrupa qoşuldu.''')

@Client.on_message(filters.command("info"))
async def _id(_, message: Message):
    msg = message.reply_to_message or message
    out_str = "**İstifadəçi Məlumatı:**\n"
    out_str += f" ⚡️ __Qrup ID__ : `{(msg.forward_from_chat or msg.chat).id}`\n"
    out_str += f" 💎 __Yanıtlanan İstifadəçi Adı__ : {msg.from_user.first_name}\n"
    out_str += f" 💬 __Mesaj ID__ : `{msg.forward_from_message_id or msg.message_id}`\n"
    if msg.from_user:
        out_str += f" 🙋🏻‍♂️ __Yanıtlanan İstifadəçi ID__ : `{msg.from_user.id}`\n"
 
    await message.reply(out_str)

@Client.on_message(filters.command("ping"))
async def pingy(client, message):
    start = datetime.now()
    hmm = await message.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await hmm.edit(
        f"█▀█ █▀█ █▄░█ █▀▀ █ \n█▀▀ █▄█ █░▀█ █▄█ ▄\n**Ping: {round(ms)}**")


class LAN(object):

    if LANGAUGE == "TR":

        BILDIRIM = "```📣 Yeni Bildirim``` \n\n#YENI_KULLANICI **botu başlattı!** \n\n🏷 isim: `{}` \n📮 kullanıcı id: `{}` \n🧝🏻‍♂️ profil linki: [{}](tg://user?id={})"
        GRUP_BILDIRIM = "```📣 Yeni Bildirim``` \n\n#YENI_GRUP **botu başlattı!** \n\n🏷 Gruba Alan İsim: `{}` \n📮 Gruba Alan kullanıcı id: `{}` \n🧝🏻‍♂️ profil linki: [{}](tg://user?id={})\n Grubun Adı: {}\n Grubun ID: {}\n Grubun Mesaj Linki( sadece açık gruplar): [Buraya Tıkla](https://t.me/c/{}/{})"
        STATS_STARTED = "{} **Lütfen bekleyiniz verileri getiriyorum!**"
        STATS = """**@{} Verileri**\n\n**Kullanıcılar;**\n» **Toplam Sohbetler:** `{}`\n» **Toplam Gruplar: `{}`\n» **Toplam PM's: `{}`\n\n**Disk Kullanımı;**\n» **Disk Alanı:** `{}`\n» **Kullanılan:** `{}({}%)`\n» **Boşta:** `{}`\n\n**🎛 En Yüksek Kullanım Değerleri;**\n» **CPU:** `{}%`\n» **RAM:** `{}%`\n**Sürümler;**\n» **Pyrogram:** {}\n\n\n__• By @BasicBots__"""
