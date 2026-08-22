from os import getenv
from dotenv import load_dotenv

load_dotenv()


def _get_int(key: str, default=None):
    """Safely convert environment variable to int."""
    value = getenv(key)
    if value is None or str(value).strip() == "":
        return default
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


# Required
API_ID = _get_int("API_ID")
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_URL = getenv("MONGO_URL")
OWNER_ID = _get_int("OWNER_ID")

# Optional
SUPPORT_GRP = getenv("SUPPORT_GRP", "")
UPDATE_CHNL = getenv("UPDATE_CHNL", "")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")

# Render / hosting (optional)
PORT = _get_int("PORT", 10000)
