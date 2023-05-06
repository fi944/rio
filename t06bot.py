from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
from config import *
import asyncio
from telethon import events
from help import *

#لايهم

c = requests.session()
bot_username3 = '@TRS04BOT'


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.بوت لايهم"))
async def _(event):
    if ispay[0] == "yes":
        await event.edit('TRS04BOT')
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع لايهم"))
async def _(event):
    if ispay[0] == "yes":
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء(@R5RR5)")
        channel_entity = await sedthon.get_entity(bot_username3)
        await sedthon.send_message('@TRS04BOT', '/start')
        await asyncio.sleep(10)
        msg0 = await sedthon.get_messages('@TRS04BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(10)
        msg1 = await sedthon.get_messages('@TRS04BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if ispay[0] == 'no':
                break
            await asyncio.sleep(10)

            list = await sedthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('(@R5RR5)لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sedthon.send_message(event.chat_id, f"مافي قنوات بلبوت")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sedthon(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sedthon(ImportChatInviteRequest(bott))
                msg2 = await sedthon.get_messages('@TRS04BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await sedthon.send_message(event.chat_id, f"تم الاشتراك في {chs} قناة")
            except:
                await sedthon.send_message(event.chat_id, f"خطأ , ممكن تبندت(@R5RR5)")
                break
        await sedthon.send_message(event.chat_id, "تم الانتهاء من التجميع !(@R5RR5)")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")

#الازرق

c = requests.session()
bot_username = '@MARKTEBOT'


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.بوت الازرق"))
async def _(event):
    if ispay[0] == "yes":
        await event.edit('MARKTEBOT')
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع الازرق"))
async def _(event):
    if ispay[0] == "yes":
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء(@R5RR5)")
        channel_entity = await sedthon.get_entity(bot_username)
        await sedthon.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(10)
        msg0 = await sedthon.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(10)
        msg1 = await sedthon.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if ispay[0] == 'no':
                break
            await asyncio.sleep(10)

            list = await sedthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('(@R5RR5)لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sedthon.send_message(event.chat_id, f"مافي قنوات بلبوت")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sedthon(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sedthon(ImportChatInviteRequest(bott))
                msg2 = await sedthon.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await sedthon.send_message(event.chat_id, f"تم الاشتراك في {chs} قناة")
            except:
                await sedthon.send_message(event.chat_id, f"خطأ , ممكن تبندت(@R5RR5)")
                break
        await sedthon.send_message(event.chat_id, "تم الانتهاء من التجميع !(@R5RR5)")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")

#المليون

c = requests.session()
bot_username1 = '@L5hbot'


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.بوت المليون"))
async def _(event):
    if ispay[0] == "yes":
        await event.edit('L5hbot')
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليون"))
async def _(event):
    if ispay[0] == "yes":
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء (@R5RR5)")
        channel_entity = await sedthon.get_entity(bot_username1)
        await sedthon.send_message('@L5hbot', '/start')
        await asyncio.sleep(10)
        msg0 = await sedthon.get_messages('@L5hbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(10)
        msg1 = await sedthon.get_messages('@L5hbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if ispay[0] == 'no':
                break
            await asyncio.sleep(10)

            list = await sedthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find(' (@R5RR5)لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sedthon.send_message(event.chat_id, f"مافي قنوات بلبوت")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sedthon(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sedthon(ImportChatInviteRequest(bott))
                msg2 = await sedthon.get_messages('@L5hbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await sedthon.send_message(event.chat_id, f"تم الاشتراك في {chs} قناة")
            except:
                await sedthon.send_message(event.chat_id, f"خطأ , ممكن تبندت (@R5RR5)")
                break
        await sedthon.send_message(event.chat_id, "تم الانتهاء من التجميع !(@R5RR5)")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")

#الجوكر

c = requests.session()
bot_username2 = '@A_MAN9300BOT'


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.بوت الجوكر"))
async def _(event):
    if ispay[0] == "yes":
        await event.edit('A_MAN9300BOT')
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع الجوكر"))
async def _(event):
    if ispay[0] == "yes":
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء (@R5RR5)")
        channel_entity = await sedthon.get_entity(bot_username2)
        await sedthon.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(10)
        msg0 = await sedthon.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(10)
        msg1 = await sedthon.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if ispay[0] == 'no':
                break
            await asyncio.sleep(10)

            list = await sedthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find(' (@R5RR5) لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sedthon.send_message(event.chat_id, f"مافي قنوات بلبوت")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sedthon(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sedthon(ImportChatInviteRequest(bott))
                msg2 = await sedthon.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await sedthon.send_message(event.chat_id, f"تم الاشتراك في {chs} قناة")
            except:
                await sedthon.send_message(event.chat_id, f"خطأ , ممكن تبندت(@R5RR5)")
                break
        await sedthon.send_message(event.chat_id, "تم الانتهاء من التجميع !(@R5RR5)")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")

#العرب

c = requests.session()
bot_username3 = '@xnsex21bot'


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.بوت العرب"))
async def _(event):
    if ispay[0] == "yes":
        await event.edit('xnsex21bot')
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع العرب"))
async def _(event):
    if ispay[0] == "yes":
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء(@R5RR5)")
        channel_entity = await sedthon.get_entity(bot_username3)
        await sedthon.send_message('@xnsex21bot', '/start')
        await asyncio.sleep(10)
        msg0 = await sedthon.get_messages('@xnsex21bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(10)
        msg1 = await sedthon.get_messages('@xnsex21bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if ispay[0] == 'no':
                break
            await asyncio.sleep(10)

            list = await sedthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('(@R5RR5)لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sedthon.send_message(event.chat_id, f"مافي قنوات بلبوت")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sedthon(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sedthon(ImportChatInviteRequest(bott))
                msg2 = await sedthon.get_messages('@xnsex21bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await sedthon.send_message(event.chat_id, f"تم الاشتراك في {chs} قناة")
            except:
                await sedthon.send_message(event.chat_id, f"خطأ , ممكن تبندت(@R5RR5)")
                break
        await sedthon.send_message(event.chat_id, "تم الانتهاء من التجميع !(@R5RR5)")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


#المليار

c = requests.session()
bot_username = '@t06bot'


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.بوت المليار"))
async def _(event):
    if ispay[0] == "yes":
        await event.edit('t06bot')
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


@sedthon.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليار"))
async def _(event):
    if ispay[0] == "yes":
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء (@R5RR5)")
        channel_entity = await sedthon.get_entity(bot_username)
        await sedthon.send_message('@t06bot', '/start')
        await asyncio.sleep(2)
        msg0 = await sedthon.get_messages('@t06bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(7)
        msg1 = await sedthon.get_messages('@t06bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(10000):
            if ispay[0] == 'no':
                break
            await asyncio.sleep(7)

            list = await sedthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه (@R5RR5)') != -1:
                await sedthon.send_message(event.chat_id, f"مافي قنوات بلبوت")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sedthon(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sedthon(ImportChatInviteRequest(bott))
                msg2 = await sedthon.get_messages('@t06bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await sedthon.send_message(event.chat_id, f"تم الاشتراك في {chs} قناة")
            except:
                await sedthon.send_message(event.chat_id, f" خطأ , ممكن تبندت (@R5RR5)")
                break
        await sedthon.send_message(event.chat_id, "تم الانتهاء من التجميع !(@R5RR5)")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")

    
@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "riojh1" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f""".تجميع المليار""")

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "riojh2" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""
        

    .تجميع المليون
    
    """)

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "riojh3" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""

      .تجميع الازرق
        
""")

@sedthon.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "RioKillerrrrrr" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await sedthon.send_message(event.chat_id, f"""

      تابع الى ريو   
        
""")