# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "23248375")

API_HASH = os.environ.get("API_HASH", "e4bc89b871fd85180f3573ede4a6a409")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6822453723:AAGBBDowoAK8fUSKai5w_ptyZIDgqpKOxJc") 

FORCE_SUB = os.environ.get("FORCE_SUB", "jaikumar_rename") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Jaikumar4220")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://VijayKumar422000:Vijaykumar4220@jaikumar4220.rlxk6yn.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6970016381').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
