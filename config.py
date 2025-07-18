import os
class Config:   
    APP_ID = int(os.environ.get("APP_ID"))
    API_HASH = os.environ.get("API_HASH")
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN") # "6658841062:AAFDWIgbflwa0sedHXoXqycHL_Mnz85h7TU") 
    OWNER_ID = os.environ.get("OWNER_ID", "")
    DATABASE_URI = os.environ.get("DATABASE_URI", "")
    TO_CHANNEL = int(os.environ.get("APP_ID"))
