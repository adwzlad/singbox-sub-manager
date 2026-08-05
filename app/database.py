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

    "sqlite:///"

    +

    str(

        settings.DATABASE_FILE

    )

)









engine = create_engine(

    DATABASE_URL,

    connect_args={

        "check_same_thread":

        False

    }

)









SessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine

)









Base = declarative_base()









# =========================
# 初始化数据库
# =========================

def init_db():


    # 确保模型注册

    from app import models


    Base.metadata.create_all(

        bind=engine

    )









# =========================
# FastAPI依赖
# =========================

def get_db():


    db = SessionLocal()



    try:


        yield db



    finally:


        db.close()
