class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6087651372"
    sudo_users = "6845325416", "6765826972"
    GROUP_ID = -1002316438413
    TOKEN = "7785998273:AAHER3KsHxhsZG2JFlA9uUOfeY0qwFW8i1c"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://graph.org/file/22da00af02bae0333df5d-457ce8b8c6a3d67e24.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "https://t.me/harddubber4"
    UPDATE_CHAT = "Collect_em_support"
    BOT_USERNAME = "http://t.me/Waifugrab17bot"
    CHARA_CHANNEL_ID = "-1002133191051"
    api_id = 29830137
    api_hash = "4fdb6b13530915e7b513ee4318f109b9"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
