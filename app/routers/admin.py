from fastapi import (

    APIRouter,

    Depends

)


from sqlalchemy.orm import Session



from app.database import get_db


from app.models import SubscriptionToken


from app.security import (

    verify_admin_key,

    create_token,

    hash_token

)







router = APIRouter(

    prefix="/admin",

    tags=["admin"]

)









# =========================
# 创建订阅Token
# =========================

@router.post(

    "/token/create"

)

def create_subscription_token(

    name:str,

    db:Session=Depends(get_db),

    _=Depends(verify_admin_key)

):


    token=create_token()



    record=SubscriptionToken(

        name=name,

        token_hash=hash_token(

            token

        )

    )



    db.add(

        record

    )


    db.commit()



    db.refresh(

        record

    )



    return {


        "id":record.id,


        "name":record.name,


        "token":token,


        "url":

        "/sub/"+token

    }









# =========================
# Token列表
# =========================

@router.get(

    "/tokens"

)

def list_tokens(

    db:Session=Depends(get_db),

    _=Depends(verify_admin_key)

):


    tokens=db.query(

        SubscriptionToken

    ).all()



    return [

        {


            "id":t.id,


            "name":t.name,


            "enabled":t.enabled,


            "created_at":

            t.created_at

        }


        for t in tokens

    ]









# =========================
# 删除Token
# =========================

@router.delete(

    "/token/{token_id}"

)

def delete_token(

    token_id:int,

    db:Session=Depends(get_db),

    _=Depends(verify_admin_key)

):


    token=db.query(

        SubscriptionToken

    ).filter(

        SubscriptionToken.id

        ==

        token_id

    ).first()



    if token:


        db.delete(

            token

        )


        db.commit()



    return {


        "success":True

    }
