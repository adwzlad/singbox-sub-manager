from sqlalchemy import create_engine

from sqlalchemy.orm import (

    sessionmaker,

    declarative_base

)



from app.config import settings







# =========================
# SQLite连接
# =========================


DATABASE_URL = (

    f"sqlite:///{settings.DATABASE_FILE}"

)





engine = create_engine(

    DATABASE_URL,

    connect_args={

        "check_same_thread": False

    }

)









# =========================
# Session
# =========================


SessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine

)









# =========================
# ORM Base
# =========================


Base = declarative_base()










# =========================
# 获取数据库Session
# =========================


def get_db():

    db = SessionLocal()


    try:

        yield db


    finally:

        db.close()










# =========================
# 初始化数据库
# =========================


def init_db():


    from app import models


    Base.metadata.create_all(

        bind=engine

    )
