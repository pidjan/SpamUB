version = "1.0.0"
import asyncio
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.enums import ParseMode
from dotenv import load_dotenv
from os import getenv
from re import split

load_dotenv()
prefix = getenv("PREFIX")
api_id = getenv("API_ID")
api_hash = getenv("API_HASH")
phone_number = getenv("PHONE_NUMBER")
app = Client(
    "do-not-delete",
    api_id,
    api_hash,
    phone_number=phone_number,
    app_version=version,
    device_model=f"SpamUB {version}",
)


@app.on_message(filters.command(["спам", "spam"], prefix) & filters.me)
async def spam(client, msg):
    await msg.edit("🌘<i>Please wait...</i>", parse_mode=ParseMode.HTML)
    splitted = split("\s+", msg.text)
    del splitted[0]
    count, *message = splitted
    message = " ".join(message)
    for i in range(int(count)):
        await app.send_message(msg.chat.id, message)
    await msg.delete()


@app.on_message(filters.command(["зспам", "dspam"], prefix) & filters.me)
async def dspam(client, msg):
    await msg.edit("🌘<i>Please wait...</i>", parse_mode=ParseMode.HTML)
    splitted = split("\s+", msg.text)
    del splitted[0]
    delay, count, *message = splitted
    message = " ".join(message)
    for i in range(int(count)):
        await app.send_message(msg.chat.id, message)
        await asyncio.sleep(float(delay))
    await msg.delete()


@app.on_message(filters.command(["spamub", "about"], prefix) & filters.me)
async def about(client, msg):
    await msg.edit(
        f"ℹ️About Spam UserBot:\n\n🌒Current version: {version}\n👑Current user: @{msg.from_user.username}\n👾Created by @pidjan\n\n📦Commands:\n\n▫️{prefix}spam &lt;count&gt; &lt;message&gt;\n▫️{prefix}dspam &lt;delay-per-message&gt; &lt;count&gt; &lt;message&gt;\n▫️{prefix}about"
    )


app.run()
