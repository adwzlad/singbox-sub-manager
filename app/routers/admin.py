from fastapi import (

    APIRouter,

    Depends

)



from app.security import (

    verify_admin_key,

    create_token

)





router = APIRouter(

    prefix="/admin",

    tags=["admin"]

)









# =========================
# 测试管理KEY
# =========================

@router.get(

    "/check"

)

def check_admin(

    _ = Depends(

        verify_admin_key

    )

):


    return {


        "success": True,


        "message":

        "admin key ok"

    }









# =========================
# 创建SUB TOKEN
# =========================

@router.post(

    "/token"

)

def create_subscription_token(

    _ = Depends(

        verify_admin_key

    )

):


    token=create_token()



    return {


        "token": token

    }
