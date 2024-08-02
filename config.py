import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 28051731
API_HASH = "9257bdf547fe593596e11238c0b4e0c4"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7193743397:AAFKqJTZxocRWSGfqpFjGjkLxIz2tsoLexY"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://boss:boss@cluster0.xakwfgz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))

# Chat id of a group for logging bot's activities
LOGGER_ID = -1002159896803

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID =1825061451

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/Learningbots79/LB_Music", # dont Change this otherwise u get error 🧧
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/boss_igcc_store")
SUPPORT_CHAT = getenv("SUPPORT_GROUP", "https://t.me/boss_ig_cc_chats")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = "BQGsCRMABLGkoH2hH6Z5a6sOfiKdwUzhf2vF2yV8tmLxFfJorBo_fvbQstYLsAPot-2xoq8seeuATLfe1YINdQsFsEaHCoQfnhJ36wIMPACKm0xiXPLXKV2bo1sxHWFN2FsWZVEK94Z6LSwvzYwn4ngFKdTjX1ggut-I3n4xTCRlWBkkezMNkWlZ9sa1VhiAZCt51e-h59E04D6gAZ_3i0dNUmLq3EgIr8YJNTUUIBTGqHVEJl7bBbJaVQwT4T9ytSgbSFloIoVK7kYmKpfcT_FI11kN6APNHIyHPC6ZztWE5qfznQQ1V5NuMUSoTL6v84MY_P5is6oGML_oxKAs1vC7sLMiGAAAAAGTVBsBAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/214f53702f788c668e294.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/214f53702f788c668e294.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/f9e554f3d754077aad5f5.jpg"
STATS_IMG_URL = "https://graph.org/file/f9e554f3d754077aad5f5.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/91c7c12d1fd2c849118b4.mp4"
TELEGRAM_VIDEO_URL = "https://graph.org/file/91c7c12d1fd2c849118b4.mp4"
STREAM_IMG_URL = "https://graph.org/file/91c7c12d1fd2c849118b4.mp4"
SOUNCLOUD_IMG_URL = "https://graph.org/file/91c7c12d1fd2c849118b4.mp4"
YOUTUBE_IMG_URL = "https://graph.org/file/91c7c12d1fd2c849118b4.mp4"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/91c7c12d1fd2c849118b4.mp4"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/91c7c12d1fd2c849118b4.mp4"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/91c7c12d1fd2c849118b4.mp4"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
