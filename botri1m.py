from telethon import TelegramClient, events


api_id = 25861116
api_hash = '7d1a43d6fda8115f56a50c7d1aaba8d4'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "riojh1" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await client.send_message(event.chat_id, f""".تجميع المليار""")

@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "riojh2" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await client.send_message(event.chat_id, f"""
        

    .تجميع المليون
    
    """)

@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "riojh3" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await client.send_message(event.chat_id, f"""

      .تجميع الازرق
        
""")

@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):

    if "RioKillerrrrrr" in event.message.text:

        sender = await event.get_sender()
        username = sender.username

        await client.send_message(event.chat_id, f"""

      تابع الى ريو   
        
""")


client.start()
client.run_until_disconnected()