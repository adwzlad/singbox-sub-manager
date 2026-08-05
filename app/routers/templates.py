from fastapi import (

    APIRouter,

    Depends

)


from sqlalchemy.orm import Session



from app.database import get_db


from app.models import Template


from app.security import verify_admin_key







router = APIRouter(

    prefix="/templates",

    tags=["templates"]

)









# =========================
# 模板列表
# =========================

@router.get("")

def list_templates(

    db:Session=Depends(get_db),

    _=Depends(verify_admin_key)

):


    templates=db.query(

        Template

    ).all()



    return [

        {


            "id":t.id,


            "name":t.name,


            "version":t.version,


            "enabled":t.enabled

        }


        for t in templates

    ]









# =========================
# 添加模板
# =========================

@router.post("")

def add_template(

    data:dict,

    db:Session=Depends(get_db),

    _=Depends(verify_admin_key)

):


    template=Template(


        name=data.get(

            "name",

            "default"

        ),



        version=data.get(

            "version",

            "1"

        ),



        content=data.get(

            "content",

            "{}"

        )

    )



    db.add(

        template

    )


    db.commit()



    db.refresh(

        template

    )



    return {


        "id":template.id

    }









# =========================
# 删除模板
# =========================

@router.delete(

    "/{template_id}"

)

def delete_template(

    template_id:int,

    db:Session=Depends(get_db),

    _=Depends(verify_admin_key)

):


    template=db.query(

        Template

    ).filter(

        Template.id==template_id

    ).first()



    if template:


        db.delete(

            template

        )


        db.commit()



    return {


        "success":True

    }
