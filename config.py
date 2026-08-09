from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "0"))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "7302427268"))
SUPPORT_GRP = getenv("SUPPORT_GRP", "")
UPDATE_CHNL = getenv("UPDATE_CHNL", "")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")
