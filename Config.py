import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "8913469"))
    API_HASH = os.environ.get("API_HASH", "b3f7cb5deefe1cf33bebee944915061b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2124064704:AAG-_oWI2-08SAgg1GbrU45OayzAHepIdAk")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOHYBu1i3RnJrMgLecVh2h8a9K8VheN55se9fg7wOzYlxcOxQSyxjWL2H1HfSuFJ3_rhsK4Xprap19GzZq8iAqexof-B3Ld6XXwQ5gtrMFnvT91wRwv3DVDad_pweHcYtdmNIoqtKU0CDg5GQJVZqkS9qSUeiJvVHogZmmTLdRXvqzCqqJsnR9e7mj-zYCyLs-9EJO5hclAAdJdjmTWa3taIwmSwXOyGhYxgmAqQn6qQn2gaolswuUTLxAq-PhwOywAUXioXWxsTKxpcoPaQLON3sjiPIJBUUGwJukppnRz4Dhb4uNNEePno8kFeoDJ8KXNEi3szddQNBLdTEP2MCJKYI2b4=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "AngelxRobot")
    SUPPORT = os.environ.get("SUPPORT", "angelsupports") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "angel_updates") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/be58748bc2dabc2d3ef4c.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
