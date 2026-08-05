import json

from datetime import datetime


from sqlalchemy.orm import Session



from app.models import (

    Template,

    Node,

    Host,

    Config

)


from app.config import settings







def replace_host(

    outbound: dict,

    hosts

):


    server = outbound.get(

        "server"

    )


    if not server:

        return outbound



    for host in hosts:


        if (

            host.enabled

            and

            host.domain == server

        ):


            outbound["server"] = host.ip


            break



    return outbound







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





    config = json.loads(

        template.content

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





    outbounds = []





    for node in nodes:


        outbound = json.loads(

            node.outbound

        )



        outbound = replace_host(

            outbound,

            hosts

        )



        outbound["tag"] = (
            node.name
            or
            f"{node.protocol}-{node.id}"
        )



        outbounds.append(

            outbound

        )





    # 保留模板基础出站

    base_outbounds = []



    for item in config.get(

        "outbounds",

        []

    ):


        if item.get(

            "type"

        ) not in [


            "vless",

            "vmess",

            "trojan",

            "tuic",

            "hysteria2",

            "anytls",

            "shadowsocks"

        ]:


            base_outbounds.append(

                item

            )





    config["outbounds"] = (

        base_outbounds

        +

        outbounds

    )









    filename = (

        name

        +

        "_"

        +

        str(

            int(

                datetime.utcnow().timestamp()

            )

        )

        +

        ".json"

    )



    filepath = (

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





    record = Config(

        name=name,

        template_id=template_id,

        file_path=str(filepath)

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
