import json


from fastapi import (

    APIRouter,

    HTTPException

)


from fastapi.responses import (

    JSONResponse

)


from pathlib import Path



from app.config import settings





router = APIRouter(

    prefix="/sub",

    tags=["subscribe"]

)









# =========================
# Token订阅
# =========================

@router.get(

    "/{token}"

)

def subscription(

    token: str

):


    config_dir = Path(

        settings.CONFIG_DIR

    )



    files = sorted(

        config_dir.glob(

            "*.json"

        ),

        key=lambda x:x.stat().st_mtime,

        reverse=True

    )





    if not files:


        raise HTTPException(

            status_code=404,

            detail="config not found"

        )





    config_file = files[0]





    with open(

        config_file,

        "r",

        encoding="utf-8"

    ) as f:


        config=json.load(f)





    return JSONResponse(

        content=config

    )
