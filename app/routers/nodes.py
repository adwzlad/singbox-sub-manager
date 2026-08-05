from fastapi import (

    APIRouter,

    Depends,

    HTTPException

)


from sqlalchemy.orm import Session



from app.database import get_db


from app.models import (

    Node,

    Subscription

)


from app.security import verify_admin_key


from app.services.updater import (

    update_subscription

)





router = APIRouter(

    prefix="/nodes",

    tags=["nodes"]

)









# =========================
# 节点列表
# =========================

@router.get("")

def list_nodes(

    db: Session = Depends(get_db),

    _ = Depends(verify_admin_key)

):


    nodes = db.query(

        Node

    ).all()



    return [

        {


            "id": node.id,


            "name": node.name,


            "protocol": node.protocol,


            "server": node.server,


            "port": node.port,


            "enabled": node.enabled

        }

        for node in nodes

    ]









# =========================
# 节点数量
# =========================

@router.get("/count")

def node_count(

    db: Session = Depends(get_db),

    _ = Depends(verify_admin_key)

):


    count=db.query(

        Node

    ).count()



    return {


        "count": count

    }









# =========================
# 刷新订阅
# =========================

@router.post(

    "/refresh/{subscription_id}"

)

def refresh_subscription(

    subscription_id:int,

    db:Session=Depends(get_db),

    _=Depends(verify_admin_key)

):


    subscription=db.query(

        Subscription

    ).filter(

        Subscription.id == subscription_id

    ).first()



    if not subscription:


        raise HTTPException(

            status_code=404,

            detail="subscription not found"

        )



    result=update_subscription(

        db,

        subscription

    )


    return result
