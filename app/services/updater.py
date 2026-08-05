import base64

from datetime import datetime


import json


import requests



from sqlalchemy.orm import Session



from app.models import (

    Subscription,

    Node

)



from app.services.parser import parse_node







def fetch_subscription(url):


    r=requests.get(

        url,

        timeout=20,

        headers={

            "User-Agent":

            "singbox-sub-manager"

        }

    )


    r.raise_for_status()


    return r.text









def decode_content(content):


    content=content.strip()



    if "://" in content:

        return content



    try:


        return base64.b64decode(

            content

            +

            "=" *

            (-len(content)%4)

        ).decode()



    except Exception:


        return content









def extract_nodes(content):


    result=[]


    for line in content.splitlines():


        line=line.strip()



        if (

            line

            and

            "://" in line

        ):


            result.append(line)



    return result









def update_subscription(

    db:Session,

    subscription:Subscription

):


    try:


        content=fetch_subscription(

            subscription.url

        )



        content=decode_content(

            content

        )



        urls=extract_nodes(

            content

        )



        if not urls:


            return {


                "success":False,


                "message":

                "empty subscription"

            }







        new_nodes=[]



        for url in urls:


            try:


                outbound=parse_node(

                    url

                )


                new_nodes.append(

                    outbound

                )



            except Exception:


                continue





        if not new_nodes:


            return {


                "success":False,


                "message":

                "no valid nodes"

            }









        # 成功后才删除旧节点

        db.query(

            Node

        ).filter(

            Node.subscription_id

            ==

            subscription.id

        ).delete()









        for outbound in new_nodes:


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







        subscription.last_update=(

            datetime.utcnow()

        )



        db.commit()



        return {


            "success":True,


            "nodes":

            len(new_nodes)

        }







    except Exception as e:



        db.rollback()



        return {


            "success":False,


            "message":

            str(e)

        }
