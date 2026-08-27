import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from bot_logic import (
    validate_text,
    build_qa_prompt,
    build_summary_prompt,
)
from gemini_service import GeminiService


# Load environment variables from .env
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.7-flash")


# Check required environment variables
if not DISCORD_TOKEN:
    raise RuntimeError("DISCORD_TOKEN is not configured.")

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY is not configured.")


# Discord intents
intents = discord.Intents.default()
intents.message_content = True


# Create bot
bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# Create AI service
ai = GeminiService(
    GEMINI_API_KEY,
    GEMINI_MODEL
)


# -------------------------
# BOT READY
# -------------------------

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}.")


# -------------------------
# ASK COMMAND
# -------------------------

@bot.command(name="ask")
async def ask(ctx, *, question: str = ""):
    """Ask the AI a question."""

    if not validate_text(question):
        await ctx.send(
            "Please provide a question. "
            "Example: !ask explain recursion"
        )
        return

    try:
        response = ai.generate(
            build_qa_prompt(question)
        )

        await ctx.send(response[:1900])

    except Exception as exc:
        print("ASK ERROR:", repr(exc))
        await ctx.send(
            "The AI service is temporarily unavailable. Please try again."
        )


# -------------------------
# SUMMARIZE COMMAND
# -------------------------

@bot.command(name="summarize")
async def summarize(ctx, *, text: str = ""):
    """Summarize the supplied text."""

    if not validate_text(text):
        await ctx.send(
            "Please provide text to summarize."
        )
        return

    try:
        response = ai.generate(
            build_summary_prompt(text)
        )

        await ctx.send(response[:1900])

    except Exception as exc:
        print("SUMMARIZE ERROR:", repr(exc))
        await ctx.send(
            "The summarization service is temporarily unavailable."
        )


# -------------------------
# HELP COMMAND
# -------------------------

@bot.command(name="helpbot")
async def helpbot(ctx):
    """Show the bot's available commands."""

    await ctx.send(
        "**ChatGPT Discord Bot**\n"
        "`!ask <question>` - Ask a question\n"
        "`!summarize <text>` - Summarize text\n"
        "`!helpbot` - Show available commands"
    )


# -------------------------
# COMMAND ERROR HANDLER
# -------------------------

@bot.event
async def on_command_error(ctx, error):

    print("COMMAND ERROR:", repr(error))

    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            "Unknown command. Use `!helpbot` to see available commands."
        )

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            "Missing input. Use `!helpbot` for command examples."
        )

    else:
        # Show the actual underlying error in the terminal
        original_error = getattr(error, "original", error)
        print("ORIGINAL ERROR:", repr(original_error))


# -------------------------
# START BOT
# -------------------------

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
