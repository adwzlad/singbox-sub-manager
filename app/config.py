import os

from pathlib import Path







# =========================
# 项目根目录
# =========================

BASE_DIR = Path(

    __file__

).resolve().parent.parent







# =========================
# 数据目录
# =========================

DATA_DIR = Path(

    os.getenv(

        "DATA_DIR",

        BASE_DIR / "data"

    )

)





DATA_DIR.mkdir(

    parents=True,

    exist_ok=True

)









# =========================
# 配置输出目录
# =========================

CONFIG_DIR = DATA_DIR / "configs"



CONFIG_DIR.mkdir(

    parents=True,

    exist_ok=True

)









class Settings:



    APP_NAME = os.getenv(

        "APP_NAME",

        "singbox-sub-manager"

    )



    VERSION = os.getenv(

        "VERSION",

        "1.0.0"

    )





    # 数据库

    DATABASE_FILE = DATA_DIR / "app.db"





    # 管理KEY

    ADMIN_KEY = os.getenv(

        "ADMIN_KEY",

        "change-me"

    )





    # Web目录

    WEB_DIR = os.getenv(

        "WEB_DIR",

        BASE_DIR / "web"

    )





    # 配置目录

    CONFIG_DIR = CONFIG_DIR







settings = Settings()
