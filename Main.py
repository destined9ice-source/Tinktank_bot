import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Your bot token go dey for Secrets, not here
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ============= THINK TANK BRAIN =============
SYSTEM_PROMPT = """
You are Think Tank AI, built by a UNIBEN Petroleum Engineer in Ugbowo, Benin City.
Your job: Help Nigerian students (JSS3 to 300L) THINK, BUILD, BECOME.

Rules:
- Speak like senior brother, simple, encouraging, small pidgin allowed
- Always give 1 actionable step, not long sermon
- Pillars: THINK = critical thinking / study hack, BUILD = Canva, AI, monetizable skill, BECOME = finished work, identity in Christ, hearing Holy Spirit
- If question about exam, use Feynman technique
- Keep answer under 150 words unless asked for more
"""

# Simple AI without OpenAI for now - you fit upgrade later
def think_tank_reply(user_text):
    text = user_text.lower()
    if "fluid" in text or "thermo" in text or "maths" in text or "exam" in text or "pass" in text:
        return (
            "🧠 THINK MODE:\n\n"
            "No dey cram. Do this:\n"
            "1. Write the topic for JSS2 pikin for paper\n"
            "2. Where you stuck = where you never understand\n"
            "3. Draw am, no just read am\n\n"
            f"Your question: '{user_text}'\n"
            "Tell me the exact topic, I go break am with Feynman now."
        )
    elif "money" in text or "skill" in text or "canva" in text or "ai" in text:
        return (
            "🔨 BUILD MODE:\n\n"
            "As student, start with this 3-day challenge:\n"
            "Day 1: Learn Canva, design 1 flyer for Think Tank\n"
            "Day 2: Use Meta AI to write caption for am\n"
            "Day 3: Post for WhatsApp status, charge 2k for next person\n\n"
            "Which one you wan start today?"
        )
    else:
        return (
            "✨ BECOME MODE:\n\n"
            "Remember: IT IS FINISHED (John 19:30). You no dey work FOR acceptance, you dey work FROM acceptance.\n\n"
            "Today: Sit 5 mins quiet, say 'Holy Spirit, I dey listen.' Write wetin drop.\n\n"
            f"You asked: '{user_text}'\n"
            "Ask am again with /ask and I go go deeper."
        )

# ============= COMMANDS =============
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to Think Tank AI 🧠🔥\n"
        "Na senior bro for Ugbowo be this.\n\n"
        "Commands:\n"
        "/think - learn how to think & pass\n"
        "/build - skill wey dey pay as student\n"
        "/become - purpose & finished work\n"
        "/ask your question - ask me anything\n\n"
        "Example: /ask How I fit understand Thermodynamics?\n\n"
        "Wetin you wan learn today?"
    )

async def cmd_think(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧠 THINK PILLAR\n\n"
        "1. Why? No ask What alone, ask Why e dey work\n"
        "2. Feynman: Teach am to JSS2 pikin\n"
        "3. Active Recall: Close book, write wetin you remember\n\n"
        "Send /ask + your subject make we practice."
    )

async def cmd_build(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔨 BUILD PILLAR\n\n"
        "3 skills wey go give UNIBEN student money in 30 days:\n"
        "• Canva Design\n"
        "• AI Research (Meta AI + ChatGPT)\n"
        "• Teaching wetin you sabi\n\n"
        "Reply: /ask I want learn Canva"
    )

async def cmd_become(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✨ BECOME PILLAR\n\n"
        "You no be your CGPA. You be son wey Son don die for.\n"
        "John 19:30 = IT IS FINISHED\n\n"
        "Exercise now: 5 mins silence. No request. Just 'Holy Spirit, I'm listening.'\n"
        "Write wetin drop for your notes."
    )

async def cmd_ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = " ".join(context.args)
    if not question:
        question = update.message.text.replace("/ask", "").strip()
    if not question:
        await update.message.reply_text("Use am like: /ask How to pass GST?")
        return
    reply = think_tank_reply(question)
    await update.message.reply_text(reply)

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Any normal message go enter here
    reply = think_tank_reply(update.message.text)
    await update.message.reply_text(reply)

def main():
    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN not found. Add am for Secrets!")
        return
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("think", cmd_think))
    app.add_handler(CommandHandler("build", cmd_build))
    app.add_handler(CommandHandler("become", cmd_become))
    app.add_handler(CommandHandler("ask", cmd_ask))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
    print("Think Tank AI dey run...")
    app.run_polling()

if __name__ == "__main__":
    main()
