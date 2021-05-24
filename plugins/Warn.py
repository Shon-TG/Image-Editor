from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = "@CoderzHEX"
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("🤭 Sorry Dude, You are B A N N E D 🤣🤣🤣")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="𝐘𝐨𝐮 𝐦𝐮𝐬𝐭 𝐣𝐨𝐢𝐧 𝐨𝐮𝐫 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐨𝐭𝐡𝐞𝐫𝐰𝐢𝐬𝐞 𝐓𝐡𝐢𝐬 𝐛𝐨𝐚𝐭 𝐢𝐬 𝐮𝐧𝐮𝐬𝐚𝐛𝐥𝐞\n<b>ꜱʜᴀʀᴇ ᴀɴᴅ ꜱᴜᴘᴘᴏʀᴛ\n\n<a href='https://t.me/Film_zone_channels'>©ꜰɪʟᴍ ᴢᴏɴᴇ</a></b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join our channel", url=f"https://t.me/coderzhex")]
              ])
            )
            return
        except Exception:
            await update.reply_text("Something Wrong. Contact my Support Group")
            return
