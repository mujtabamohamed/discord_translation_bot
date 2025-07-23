import discord
from discord.ext import tasks, commands
from discord.utils import get
from dotenv import load_dotenv
import asyncio
import os
import googletrans 
from discord import Embed

translator = googletrans.Translator()

flag_emoji_dict = {
"🇺🇸": "en",
"🇩🇪": "de",
"🇫🇷": "fr",
"🇪🇸": "es",
"🇮🇹": "it",
"🇵🇹": "pt",
"🇷🇺": "ru",
"🇦🇱": "sq",
"🇸🇦": "ar",
"🇧🇦": "bs",
"🇧🇬": "bg",
"🇨🇳": "zh-CN",
"🇭🇷": "hr",
"🇨🇿": "cs",
"🇩🇰": "da",
"🇪🇪": "et",
"🇫🇮": "fi",
"🇬🇷": "el",
"🇭🇺": "hu",
"🇮🇩": "id",
"🇮🇳": "hi",
"🇮🇪": "ga",
"🇮🇸": "is",
"🇮🇱": "he",
"🇯🇵": "ja",
"🇰🇷": "ko",
"🇱🇻": "lv",
"🇱🇹": "lt",
"🇲🇹": "mt",
"🇲🇪": "sr",
"🇳🇱": "nl",
"🇳🇴": "no",
"🇵🇰": "ur",
"🇵🇱": "pl",
"🇵🇹": "pt",
"🇷🇴": "ro",
"🇷🇸": "sr",
"🇸🇦": "ar",
"🇸🇰": "sk",
"🇸🇮": "sl",
"🇸🇬": "sv",
"🇹🇭": "th",
"🇹🇷": "tr",
"🇹🇼": "zh-TW",
"🇺🇦": "uk",
"🇻🇦": "la"
}

load_dotenv(".env")
TOKEN = os.getenv("TOKEN")

intents=discord.Intents.all()

prefix = './'
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.emoji in flag_emoji_dict:
        lang_code = flag_emoji_dict[reaction.emoji]
        message = reaction.message
        detected_lang = translator.detect(message.content)
        translated_message = translator.translate(message.content, dest=lang_code).text
        pronunciation_message = translator.translate(message.content, dest=lang_code).pronunciation
        confidence = detected_lang.confidence if detected_lang.confidence is not None else 0.0

        embed = Embed(title='Translated Text', description=f'{translated_message}', color=0x00ff00)
        embed.add_field(name="Original Text", value=message.content, inline=False)
        embed.add_field(name="Translated from:", value=f'{detected_lang.lang.capitalize()} ({confidence*100:.2f}%)')
        embed.add_field(name="Pronunciation:", value=pronunciation_message, inline=False)
        await reaction.message.channel.send(content=f'{user.mention}', embed=embed)

bot.run(TOKEN)