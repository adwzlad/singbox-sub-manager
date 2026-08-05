from secrets import (

    token_urlsafe,

    compare_digest

)



from fastapi import (

    Header,

    HTTPException

)



from app.config import settings







# =========================
# 管理后台KEY验证
# =========================

def verify_admin_key(

    x_admin_key: str = Header(

        default=None

    )

):


    if not x_admin_key:


        raise HTTPException(

            status_code=401,

            detail="Missing admin key"

        )




    if not compare_digest(

        x_admin_key,

        settings.ADMIN_KEY

    ):


        raise HTTPException(

            status_code=403,

            detail="Invalid admin key"

        )



    return True







# =========================
# 生成SUB TOKEN
# =========================

def create_token():



    return token_urlsafe(

        32

    )









# =========================
# Token验证
# =========================

def check_token(

    token: str,

    saved_token: str

):


    return compare_digest(

        token,

        saved_token

    )
