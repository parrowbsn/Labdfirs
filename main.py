import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackContext, CallbackQueryHandler
)
from config import BOT_TOKEN, FORCE_CHANNEL  # Import from config.py
from telegram.error import BadRequest

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Start message
START_TXT = """<b> ˹ 𝗧ᴇ𝘅ᴛ 𝗧ᴇʀᴍɪɴᴀᴛᴏʀ ˼ </b>

Wᴇʟᴄᴏᴍᴇ! I ᴀᴍ ˹ 𝗧ᴇ𝘅ᴛ 𝗧ᴇʀᴍɪɴᴀᴛᴏʀ ˼, ᴡʜɪᴄʜ ᴅᴇᴛᴇᴄᴛs ᴄᴏᴘʏʀɪɢʜᴛ ᴍᴀᴛᴇʀɪᴀʟ ᴀɴᴅ ᴀᴜᴛᴏᴅᴇʟᴇᴛᴇs ɪᴛ.⚡

⚡ **Hᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ:** Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ɢɪᴠᴇ ᴍᴏᴅᴇʀᴀᴛᴏʀ ʀɪɢʜᴛs ✨"""

# Start photo
START_PHOTO_URL = "https://graph.org/file/507986c81f04c68396cef-a9f06b609e411d6481.jpg"

# Check if the user is subscribed to the channel
async def is_user_subscribed(user_id: int, context: CallbackContext) -> bool:
    try:
        # Check user's membership status in the channel
        member = await context.bot.get_chat_member(chat_id=f"@{FORCE_CHANNEL}", user_id=user_id)
        return member.status in ["member", "administrator", "creator"]
    except BadRequest:
        return False

# Start command handler
async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    user_name = update.effective_user.first_name

    # Check if the user is subscribed
    if not await is_user_subscribed(user_id, context):
        # Send force subscription message with buttons
        await update.message.reply_text(
            f"👋 Hello {user_name}!\n\nYou must join our channel to use this bot:\n"
            f"👉 [Sparrow Bots](https://t.me/{FORCE_CHANNEL})\n\n"
            "Once you have joined, click the **Verify** button below.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔔 Join Channel", url=f"https://t.me/{FORCE_CHANNEL}")],
                [InlineKeyboardButton("✅ Verify", callback_data="verify_subscription")]
            ]),
            parse_mode="Markdown"
        )
        return

    # Send the start message if subscribed
    keyboard = [
        [
            InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url=f"https://t.me/{FORCE_CHANNEL}"),
            InlineKeyboardButton("• Oᴡɴᴇʀ •", url="https://t.me/Harhsu_Raven"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_photo(
        photo=START_PHOTO_URL,
        caption=START_TXT,
        reply_markup=reply_markup,
        parse_mode="HTML"
    )

# Verify subscription callback handler
async def verify_subscription(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = query.from_user.id

    # Re-check if the user is subscribed
    if await is_user_subscribed(user_id, context):
        await query.answer("✅ Subscription verified!")
        await query.message.delete()

        # Send the start message
        keyboard = [
            [
                InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url=f"https://t.me/{FORCE_CHANNEL}"),
                InlineKeyboardButton("• Oᴡɴᴇʀ •", url="https://t.me/Harhsu_Raven"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.message.reply_photo(
            photo=START_PHOTO_URL,
            caption=START_TXT,
            reply_markup=reply_markup,
            parse_mode="HTML"
        )
    else:
        await query.answer("❌ You are not subscribed yet. Please join the channel first.", show_alert=True)

# Main function to run the bot
async def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(verify_subscription, pattern="^verify_subscription$"))

    # Start the bot
    logger.info("Bot started successfully!")
    await application.run_polling()

# Run the bot
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
