from fastapi import (

    APIRouter,

    Depends,

    HTTPException

)


from sqlalchemy.orm import Session



from app.database import get_db


from app.models import Host


from app.security import verify_admin_key







router = APIRouter(

    prefix="/hosts",

    tags=["hosts"]

)









# =========================
# Hosts列表
# =========================

@router.get("")

def list_hosts(

    db: Session = Depends(get_db),

    _ = Depends(verify_admin_key)

):


    hosts = db.query(

        Host

    ).all()



    return [

        {


            "id": h.id,


            "domain": h.domain,


            "ip": h.ip,


            "enabled": h.enabled

        }

        for h in hosts

    ]









# =========================
# 添加Hosts
# =========================

@router.post("")

def add_host(

    domain: str,

    ip: str,

    db: Session = Depends(get_db),

    _ = Depends(verify_admin_key)

):


    exists=db.query(

        Host

    ).filter(

        Host.domain == domain

    ).first()



    if exists:


        raise HTTPException(

            status_code=400,

            detail="host already exists"

        )





    host=Host(

        domain=domain,

        ip=ip

    )



    db.add(

        host

    )


    db.commit()



    db.refresh(

        host

    )



    return {


        "id": host.id,


        "domain": host.domain,


        "ip": host.ip

    }









# =========================
# 删除Hosts
# =========================

@router.delete(

    "/{host_id}"

)

def delete_host(

    host_id:int,

    db:Session=Depends(get_db),

    _=Depends(verify_admin_key)

):


    host=db.query(

        Host

    ).filter(

        Host.id == host_id

    ).first()



    if not host:


        raise HTTPException(

            status_code=404,

            detail="host not found"

        )



    db.delete(

        host

    )


    db.commit()



    return {


        "success":True

    }
