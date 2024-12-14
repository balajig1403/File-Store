import re
import os
from os import environ
from Script import script
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot Information
API_ID = int(environ.get("API_ID", "11112771"))
API_HASH = environ.get("API_HASH", "4606a7fdabe4eb7f6c0b1ce77f6372ce")
BOT_TOKEN = environ.get("BOT_TOKEN", "7932633515:AAGmfR8TPTscogWmYLMUPlxq-XkmJ4PzI6Y")

PICS = (environ.get('PICS', 'https://graph.org/file/ce1723991756e48c35aa1.jpg')).split() # Bot Start Picture
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1303617136').split()]
BOT_USERNAME = environ.get("BOT_USERNAME", "Balaji_Store_bot") # without @


# Clone Info :-
CLONE_MODE = bool(environ.get('CLONE_MODE', False)) # Set True or False
# If Clone Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
CLONE_DB_URI = environ.get("CLONE_DB_URI", "mongodb+srv://filestorebot:filestorebot@save-restricted-bot.fkdsd.mongodb.net/?retryWrites=true&w=majority&appName=Save-Restricted-Bot")
CDB_NAME = environ.get("CDB_NAME", "cfilestoredb")

# Database Information
DB_URI = environ.get("DB_URI", "mongodb+srv://filestorebot:filestorebot@save-restricted-bot.fkdsd.mongodb.net/?retryWrites=true&w=majority&appName=Save-Restricted-Bot")
DB_NAME = environ.get("DB_NAME", "filestoredb")


# Auto Delete Information
AUTO_DELETE_MODE = bool(environ.get('AUTO_DELETE_MODE', True)) # Set True or False

# If Auto Delete Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
AUTO_DELETE = int(environ.get("AUTO_DELETE", "60")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "3600")) # Time in Seconds


# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001636534856"))

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
@@ -70,7 +70,7 @@ def is_enabled(value, default):
WEBSITE_URL = environ.get("WEBSITE_URL", "") # For More Information Check Video On Yt - @Tech_VJ

# File Stream Config
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or False


# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://testofvjfilter-1fa60b1b8498.herokuapp.com/")
# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
