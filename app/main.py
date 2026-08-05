from contextlib import asynccontextmanager

from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from pathlib import Path



from app.config import settings

from app.database import init_db



from app.routers import (

    admin,

    subscribe,

    nodes,

    templates,

    hosts

)









@asynccontextmanager

async def lifespan(app: FastAPI):


    init_db()


    yield









app = FastAPI(

    title=settings.APP_NAME,

    version=settings.VERSION,

    lifespan=lifespan

)









# =========================
# API路由
# =========================


app.include_router(

    admin.router

)


app.include_router(

    subscribe.router

)


app.include_router(

    nodes.router

)


app.include_router(

    templates.router

)


app.include_router(

    hosts.router

)









# =========================
# Web静态文件
# =========================


if Path(

    settings.WEB_DIR

).exists():


    app.mount(

        "/web",

        StaticFiles(

            directory=settings.WEB_DIR,

            html=True

        ),

        name="web"

    )









@app.get("/")

def index():


    return {


        "name":

        settings.APP_NAME,


        "version":

        settings.VERSION,


        "web":

        "/web/index.html"

    }
