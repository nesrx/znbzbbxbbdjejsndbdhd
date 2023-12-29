from AlexaMusic import app
from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import upload_file
import os
from strings.filters import command


@app.on_message(command(["تليجراف ميديا","ميديا","تليكراف ميديا"]))
async def get_link_group(client, message):
    try:
        text = await message.reply("Processing...")
        async def progress(current, total):
            await text.edit_text(f" يتم رفع الوسائط ... {current * 100 / total:.1f}%")
        try:
            location = f"./media/group/"
            local_path = await message.reply_to_message.download(location, progress=progress)
            await text.edit_text(" يتم جلب الرابط ... ")
            upload_path = upload_file(local_path) 
            await text.edit_text(f" | الرابط :\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"❌ | فشل تحميل الملف\n\n<i>السبب: {e}</i>")
            os.remove(local_path) 
            return         
    except Exception:
        pass