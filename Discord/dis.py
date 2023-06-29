import discord
import asyncio

TOKEN = 'YOUR_DISCORD_TOKEN'
CHANNEL_ID = 123456789 # ID của channel Discord bạn muốn gửi tin nhắn vào

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    channel = client.get_channel(CHANNEL_ID)
    while True:
        await channel.send('hello')
        await asyncio.sleep(2) # Đợi 2 giây trước khi gửi tin nhắn tiếp theo

client.run(TOKEN)
