from pathlib import Path

from pydantic_settings import BaseSettings





# 项目根目录

BASE_DIR = Path(__file__).resolve().parent.parent





class Settings(BaseSettings):


    # =====================
    # 项目信息
    # =====================

    APP_NAME: str = "singbox-sub-manager"


    VERSION: str = "1.0.0"





    # =====================
    # 服务
    # =====================

    HOST: str = "0.0.0.0"


    PORT: int = 8080





    # =====================
    # 管理KEY
    # =====================

    ADMIN_KEY: str = "change-me"





    # =====================
    # 数据目录
    # =====================

    DATA_DIR: Path = BASE_DIR / "data"


    DATABASE_FILE: Path = (

        BASE_DIR

        /

        "data"

        /

        "app.db"

    )





    # =====================
    # Web目录
    # =====================

    WEB_DIR: Path = (

        BASE_DIR

        /

        "web"

    )





    # =====================
    # 文件目录
    # =====================

    TEMPLATE_DIR: Path = (

        BASE_DIR

        /

        "data"

        /

        "templates"

    )


    CONFIG_DIR: Path = (

        BASE_DIR

        /

        "data"

        /

        "configs"

    )





    class Config:

        env_file = ".env"





settings = Settings()





# 初始化目录

settings.DATA_DIR.mkdir(

    exist_ok=True

)


settings.TEMPLATE_DIR.mkdir(

    exist_ok=True

)


settings.CONFIG_DIR.mkdir(

    exist_ok=True

)
