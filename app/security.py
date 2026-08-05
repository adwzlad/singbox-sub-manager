import secrets

import hashlib



from fastapi import (

    Header,

    HTTPException

)



from app.config import settings









# =========================
# 管理KEY验证
# =========================

def verify_admin_key(

    x_admin_key: str = Header(None)

):


    if not x_admin_key:


        raise HTTPException(

            status_code=401,

            detail="missing admin key"

        )





    if x_admin_key != settings.ADMIN_KEY:


        raise HTTPException(

            status_code=403,

            detail="invalid admin key"

        )



    return True









# =========================
# 创建SUB TOKEN
# =========================

def create_token():



    token = secrets.token_urlsafe(

        32

    )



    return token









# =========================
# Token哈希
# =========================

def hash_token(

    token:str

):


    return hashlib.sha256(

        token.encode()

    ).hexdigest()
