import json

import os

from datetime import datetime



from sqlalchemy.orm import Session



from app.models import (

    Template,

    Node,

    Host,

    Config

)



from app.config import settings







# =========================
# Hosts替换
# =========================

def replace_hosts(

    outbound,

    hosts

):


    if not hosts:

        return outbound



    server = outbound.get(

        "server"

    )



    for host in hosts:


        if (

            host.enabled

            and

            host.domain == server

        ):


            outbound["server"] = host.ip


            break



    return outbound







# =========================
# 生成配置
# =========================

def generate_config(

    db: Session,

    template_id: int,

    name: str

):


    template = db.query(

        Template

    ).filter(

        Template.id == template_id

    ).first()



    if not template:


        raise Exception(

            "template not found"

        )





    nodes = db.query(

        Node

    ).filter(

        Node.enabled == True

    ).all()





    hosts = db.query(

        Host

    ).filter(

        Host.enabled == True

    ).all()







    config = json.loads(

        template.content

    )





    outbounds=[]



    for node in nodes:


        outbound=json.loads(

            node.outbound

        )



        outbound=replace_hosts(

            outbound,

            hosts

        )



        outbound["tag"]=node.name



        outbounds.append(

            outbound

        )





    config["outbounds"] = (

        config.get(

            "outbounds",

            []

        )

        +

        outbounds

    )







    filename=(

        f"{name}_"

        f"{int(datetime.utcnow().timestamp())}"

        ".json"

    )



    filepath=(

        settings.CONFIG_DIR

        /

        filename

    )





    with open(

        filepath,

        "w",

        encoding="utf-8"

    ) as f:


        json.dump(

            config,

            f,

            ensure_ascii=False,

            indent=2

        )







    record=Config(


        name=name,


        template_id=template_id,


        file_path=str(

            filepath

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


        "file":str(filepath)

    }
