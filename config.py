# Copyright (c) 2021 ThePro-CoderZ
# Part of: Nexa-Userbot

import os

class Config(object):
    APP_ID = os.environ.get("APP_ID", "2285397")
    API_HASH = os.environ.get("API_HASH", "636fc37d9384a91c61619953cd760b48")
    # Pyrogram Session
    PYRO_STR_SESSION = os.environ.get("PYRO_STR_SESSION", "BQCKXwdxBeJ-0lr94sjuPS-Zp2z8Lb_IxOmfG8GOnD5HBWYyOQ9qTkfj8sSza29BO8WSlIX0lllu0VTftR0fsmRU-dO4mvzEt1o7bmx8rlRgCI87FJ-XPZyMAzNeXPED9Ds6YlLz1Cb0hLj9hTpsVZELYsDNpGe_Rmc2F7PnM4hCySYTjLQuWk8ghLe-6XlTw_5-X5tqfgBjh9fVOxmP7-9osdbzO06bG0qc8MvkTWEb0UrGSuggI7ujdcxNJCCROIblUB8Xq8S9NmSIuETtJ_7rsgPa-6HQoQGs-2tO2pqz1HzzaIu8cj8XGX4d8QuwlIXBJiWxbI3azAwtjyxySsNPAAAAAd4B_cAA")
    CMD_PREFIX = os.environ.get("CMD_PREFIX", "!")
    MONGODB_URL = os.environ.get("MONGODB_URL", "mongodb+srv://pagac28482:JaltQe2DsAuJkLkO@cluster0.jm0vf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
