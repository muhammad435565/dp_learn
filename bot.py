import os
import mysql.connector
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ⛓️ MySQL Database connection
def save_user(user):
    connection = mysql.connector.connect(
        host=os.environ.get("sql311.alchosting.xyz"),
        user=os.environ.get("alcy_38988147"),
        password=os.environ.get("IyF0kBBk882hrZd"),
        database=os.environ.get("alcy_38988147_dp_learn")
    )
    cursor = connection.cursor()
    query = "INSERT INTO users (telegram_id, username, first_name) VALUES (%s, %s, %s)"
    values = (user.id, user.username, user.first_name)
    cursor.execute(query, values)
    connection.commit()
    connection.close()

# 🟢 /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    save_user(user)
    await update.message.reply_text("Hello World!")

# 🚀 Start the bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(os.environ.get("7112951421:AAEGEpHWb3dC0lPyV9qvjjUnWLZN8aw0pMs")).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot running...")
    app.run_polling()
