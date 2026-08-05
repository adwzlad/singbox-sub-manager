import json


from pathlib import Path



from fastapi import (

    APIRouter,

    HTTPException,

    Depends

)



from fastapi.responses import JSONResponse



from sqlalchemy.orm import Session



from app.database import get_db


from app.models import SubscriptionToken


from app.security import hash_token


from app.config import settings







router = APIRouter(

    prefix="/sub",

    tags=["subscribe"]

)









@router.get(

    "/{token}"

)

def subscription(

    token:str,

    db:Session=Depends(get_db)

):


    token_hash = hash_token(

        token

    )





    record = db.query(

        SubscriptionToken

    ).filter(

        SubscriptionToken.token_hash

        ==

        token_hash

    ).first()





    if not record or not record.enabled:


        raise HTTPException(

            status_code=403,

            detail="invalid token"

        )









    files = sorted(

        Path(

            settings.CONFIG_DIR

        ).glob(

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







    with open(

        files[0],

        "r",

        encoding="utf-8"

    ) as f:


        config=json.load(f)





    return JSONResponse(

        content=config

    )
