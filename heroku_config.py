import os


class Var(object):
    APP_ID = int(os.environ.get("7092919", 6))
    # 6 is a placeholder
    API_HASH = os.environ.get("API_HASH", e37661f962cc0a17e784927cfc83cac9)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOIMBuyAOZPx5R5rbmQpp-uDiax3ePYJhM958b5WIMdLfygDTeok9wArFM0Kfuwq6wm6iqCdjVAFeZa_UEzs5HkUsuDeynOmrpKjXukVlgwUdjXwTdJ-WDHZW__8OlQhIQxLeZj96L3sAoMhGtNYUM6kWnEd4N1DHG_Ddq2Jl5d2nJdFPNDGrDvVr7YfG0sM4An3w8s248uOF0jm2mYYvmWYdaSnpfOrhQIrjjUFJwxrYkp2TPpmdZ9pSS6QE9QZTKOYzzVi0i3XZJRPOHNGJ5_urpfkzbbyyd5-B4C69wDEmZbhg9nCV3h3b6bG3JijWwBKWgy-2QW-v7JSL6_H1zE3wMho=)
    DB_URI = os.environ.get("DATABASE_URL", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./userbot/DOWNLOADS/")
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Here for later purposes
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", None), 
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", a8e49d92-77f9-4f4b-8f5f-7fff9053491e)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", Userbot)
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", 2043886741:AAE87shI7sc_tzzocYvq0NBpzs3RYxZDsz0)
    # Send .get_id in any channel to fill this value.
    COMBINED_GROUP_ID = int(os.environ.get("COMBINED_GROUP_ID", -1001525112206))
    PLUGIN_CHANNEL = os.environ.get("PLUGIN_CHANNEL", f"{-1001525112206}")
    PRIVATE_GROUP_BOT_API_ID = os.environ.get("PRIVATE_GROUP_BOT_API_ID", f"{-1001525112206}")
    PM_PERMIT_GROUP_ID = os.environ.get("PM_PERMIT_GROUP_ID", f"{-1001525112206}")
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", @Satoshi1_Robot)
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
    if AUTH_TOKEN_DATA is not None:
        if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
            os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        t_file = open(TEMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", f"{-1001525112206}")
    if PRIVATE_GROUP_ID is not None:
        try:
            PRIVATE_GROUP_ID = int(-1001525112206)
        except ValueError:
            raise ValueError(
                "Invalid Private Group ID. Make sure your ID is starts with -100 and make sure that it is only numbers."
            )
    NEWS_CHANNEL_ID = int(os.environ.get("NEWS_CHANNEL_ID", -100))
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    ANTISPAM_SYSTEM = os.environ.get("ANTISPAM_SYSTEM", "DISABLE")
    LIGHTNING_PRO = os.environ.get("LIGHTNING_PRO", "YES")
    WHITE_CHAT = set(int(x) for x in os.environ.get("WHITE_CHAT", "").split())


class Development(Var):
    LOGGER = True
