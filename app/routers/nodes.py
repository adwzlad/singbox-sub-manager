from fastapi import (

    APIRouter,

    Depends

)



from sqlalchemy.orm import Session



from app.database import get_db


from app.models import Node


from app.security import verify_admin_key







router = APIRouter(

    prefix="/nodes",

    tags=["nodes"]

)









# =========================
# 节点列表
# =========================

@router.get("")

def list_nodes(

    db:Session=Depends(get_db),

    _=Depends(verify_admin_key)

):


    nodes=db.query(

        Node

    ).all()



    return [

        {


            "id":node.id,


            "name":node.name,


            "protocol":node.protocol,


            "server":node.server,


            "port":node.port,


            "enabled":node.enabled

        }


        for node in nodes

    ]









# =========================
# 节点数量
# =========================

@router.get(

    "/count"

)

def node_count(

    db:Session=Depends(get_db),

    _=Depends(verify_admin_key)

):


    count=db.query(

        Node

    ).filter(

        Node.enabled == True

    ).count()



    return {


        "count":count

    }









# =========================
# 删除节点
# =========================

@router.delete(

    "/{node_id}"

)

def delete_node(

    node_id:int,

    db:Session=Depends(get_db),

    _=Depends(verify_admin_key)

):


    node=db.query(

        Node

    ).filter(

        Node.id == node_id

    ).first()



    if node:


        db.delete(

            node

        )


        db.commit()



    return {


        "success":True

    }
