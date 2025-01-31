# Copyright (c) 2021 ThePro-CoderZ
# Part of: Nexa-Userbot
from time import time
from pyrogram import Client
from config import Config

# Configs
HELP = {}
CMD_HELP = {}
StartTime = time()

NEXAUB = Client(
    "NexaUserBot",  # Optional session name (can be any string)
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    session_string=Config.PYRO_STR_SESSION  # ✅ Corrected keyword
)
