import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = "7367548692:AAH5eklnBHQ2Q_-o_5GDcEex6HUd3Gfy_E4"
    # The Telegram API things
    API_ID = 23746596
    API_HASH = "15ce5501fd05fae38473f02a97fdf899"
    # Get these values from my.telegram.org
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 4194304000 #2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    OWNER_ID = 6116993643
    SESSION_NAME = "TCP-URLUPLOADER-BOT"
    # database uri (mongodb)
    DATABASE_URL = "mongodb+srv://shivaynetflix2:Shivay@1234@cluster0.z0uewqq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    MAX_RESULTS = "50"
    PREMIUM_USER = os.environ.get("PREMIUM_USER")
