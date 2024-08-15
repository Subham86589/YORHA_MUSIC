import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = "25355409"
API_HASH = "b9c741ba6b62f492dd0a3a39f7b2c526"
# ------------------------------------------------------
BOT_TOKEN = "7241166244:AAEK45mvVkcXNftI0tIMslmI7wVoFamoPLA"
# -------------------------------------------------------
OWNER_USERNAME = "Whotf_iz_Subbu"
# --------------------------------------------------------
BOT_USERNAME = "Yorha2bXMusicBot"
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "Nexiko")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "MissYumikoo")
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority"
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", -1002147996645))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 7218905176))
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Subham86589/YORHA_MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/BILLA_GANG_NETWORK")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/BILLA_GANG_NTWK")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = "BQGC5JEAipyCiEJrhdaj56gsdXUExHomH6-LY74S15B4oy8NlIl0_hKkmBfqytH85-XFUDQrqOfdFFsmjugdITl_QF1VTwA1TvV7_qPIDWdLjnEVfZmlsxXMwAlfHvVj9Ni44A2ps_FoqsuVCFfckkCeYJ-dlUqLIirCS8ADV0O2d_BxeXprft_mHoFM2tDP1GFPK8fGn0bMOij4z9hgrFLQlgfQk3mUsTxhpi8QURnsccq3OKv8_HZcmqF3_y_3dGH06m0stnLpUlMdXCG9m0sTqOUog19LNoIV3LgHujhVCst-RmPHLlXoYJ4C72AAStllzUkEKpn2OYccnTN0BMN4AZLxSQAAAAGSB6FlAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/7a80885bf6bfa2ca642a4.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/a0c6b6ac76f8bf4fe0bc9.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/a83b19b22889481cd54f6.jpg"
STATS_IMG_URL = "https://telegra.ph/file/1e9037b86c896dc629aa5.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/666b4ce78ff92d6ed27af.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/1e9037b86c896dc629aa5.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/a0c6b6ac76f8bf4fe0bc9.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/7a80885bf6bfa2ca642a4.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/a0c6b6ac76f8bf4fe0bc9.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/1e9037b86c896dc629aa5.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/666b4ce78ff92d6ed27af.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/519160c46f395317c6688.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
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
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
