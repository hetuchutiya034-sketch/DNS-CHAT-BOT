from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "21552265"
# -------------------------------------------------------------
API_HASH = "1c971ae7e62cc416ca977e040e700d09"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "7408008545"))
SUPPORT_GRP = "RU_DRA_098"
UPDATE_CHNL = "RU_DRA_098"
OWNER_USERNAME = "RU_DRA_65"
