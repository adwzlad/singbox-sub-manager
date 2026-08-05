import base64

import json

import requests



from datetime import datetime



from sqlalchemy.orm import Session



from app.models import (

    Subscription,

    Node

)



from app.services.parser import parse_node







# =========================
# 获取订阅内容
# =========================

def fetch_subscription(url: str):


    response = requests.get(

        url,

        timeout=20,

        headers={

            "User-Agent":

            "singbox-sub-manager"

        }

    )


    response.raise_for_status()


    return response.text







# =========================
# 解码
# =========================

def decode_content(content: str):


    content = content.strip()



    # 已经是明文URL

    if "://" in content:

        return content





    try:


        decoded = base64.b64decode(

            content +

            "=" *

            (-len(content) % 4)

        ).decode(

            "utf-8"

        )


        return decoded



    except Exception:


        return content







# =========================
# 分割节点
# =========================

def extract_nodes(content: str):


    result=[]



    for line in content.splitlines():


        line=line.strip()



        if not line:

            continue



        if "://" in line:


            result.append(

                line

            )


    return result







# =========================
# 更新订阅
# =========================

def update_subscription(

    db: Session,

    subscription: Subscription

):


    content = fetch_subscription(

        subscription.url

    )



    content = decode_content(

        content

    )



    urls = extract_nodes(

        content

    )





    # 删除旧节点

    db.query(

        Node

    ).filter(

        Node.subscription_id

        ==

        subscription.id

    ).delete()





    count=0



    for url in urls:


        try:


            outbound=parse_node(

                url

            )



            node=Node(


                subscription_id=

                subscription.id,



                name=

                outbound.get(

                    "server",

                    "unknown"

                ),



                protocol=

                outbound.get(

                    "type"

                ),



                server=

                outbound.get(

                    "server"

                ),



                port=

                outbound.get(

                    "server_port"

                ),



                outbound=json.dumps(

                    outbound,

                    ensure_ascii=False

                )

            )



            db.add(

                node

            )


            count += 1



        except Exception:


            # 单节点失败跳过

            continue





    subscription.last_update = (

        datetime.utcnow()

    )



    db.commit()



    return {


        "success": True,


        "nodes": count

    }
