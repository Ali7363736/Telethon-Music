import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "15690119"))
    API_HASH = os.environ.get("API_HASH", "906cbd992a4257f9f569a337ea8d69f8")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5919103632:AAELGvQG5u-QynP2Ru6KBeskOE5TclxQ5TI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "AgAwl8TzNW_jJT47Npbf5rJA8I6lBjDuQe9R88jTdFubj0i4ULTGdisU7lFSCaVRO0sUt87z3XfXj3-r174ssXTPAzX2smH8V4-k4HWw6sWrZLkY3xpokjXeMrilbjjGmIHsAXDsp9PNDxzxpBF1SnT8--oAfv6Ad50qlrQFYEVNT2O0vE8EuUlHvF9RpFwNDh3JhUPVzRgRxmxxQFEarpI9ZZCPOtrnVqreyipM_9wQLjWpDlMWsov8pd03Qi6_RqH2kMRVwJvXoq5kvZw8lSGJayQvI7XJQ0pCs2EKDW9G3MX6chzmeZxarGG2lxE87zM9HFUg1mR6wg1gdB5E3eA9MAS5RQA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "HerozMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
