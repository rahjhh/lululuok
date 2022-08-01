import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
if os.path.exists("Internal"):
    load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
admins = {}
que = {}

API_ID = int(getenv("API_ID", "1271075"))
API_HASH = getenv("API_HASH", "b6c77f69fd2cb71da521dcfc41233e50")
BOT_TOKEN = getenv("BOT_TOKEN", "5592359774:AAEp9_ib_9CtDrDAhd6NlNnd4F-cYOQ1nyQ")
STRING_SESSION = getenv("STRING_SESSION", "1BVtsOHUBuzrgL4IHDKnjlJcZKJ0UL8pJJMHylLstMgEV5cnhH1iU_pnGOCSEHMcjyUab0AalC_jpQCqgiydmWMGUenNKqbmUlObwrrdrhNw4PYX7TByfa_f3rQk8vRaMvF5FHrUJwcbS7ZEhT39u3sJ1Zt0q0sEW1IML5a0sVcEjFe-nVR96HOBAieAbCzyMir44jfwx2TDCWD6qPJaUWTkKn9kLFa7etm2qgoIerGfzFMIFzFz2cSF2d6R_DdpMGc-cJAa1dXvSc8Bya4qKxQ9Tq9bZt1oYgwyuJwsgC8haiuDBsY9731Ecgh7AIXIZJ52U_RFftbPPGOHBFAAy2XUdBCfWkx8=")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! /").split())
MONGO_DB_URL = getenv("MONGO_DB_URL", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1163549470").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1163549470").split()))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/GeniusBoi/Genius-Userbot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "aditya")
