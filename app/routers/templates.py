from fastapi import (

    APIRouter,

    Depends,

    HTTPException,

    UploadFile,

    File

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

    db: Session = Depends(get_db),

    _ = Depends(verify_admin_key)

):


    templates = db.query(

        Template

    ).all()



    return [

        {


            "id": t.id,


            "name": t.name,


            "version": t.version,


            "enabled": t.enabled

        }

        for t in templates

    ]









# =========================
# 上传模板
# =========================

@router.post(

    "/upload"

)

async def upload_template(

    file: UploadFile = File(...),

    db: Session = Depends(get_db),

    _ = Depends(verify_admin_key)

):


    content = await file.read()



    try:


        text = content.decode(

            "utf-8"

        )



    except Exception:


        raise HTTPException(

            status_code=400,

            detail="invalid file"

        )





    template = Template(

        name=file.filename,


        content=text

    )



    db.add(

        template

    )


    db.commit()



    db.refresh(

        template

    )



    return {


        "id": template.id,


        "name": template.name

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

        Template.id == template_id

    ).first()



    if not template:


        raise HTTPException(

            status_code=404,

            detail="template not found"

        )



    db.delete(

        template

    )


    db.commit()



    return {


        "success": True

    }
