from urllib.parse import urlsplit, parse_qs

import base64

import json







def params(url):

    return {

        k:v[0]

        for k,v in parse_qs(

            urlsplit(url).query

        ).items()

    }









def parse_vless(url):


    u=urlsplit(url)

    p=params(url)



    tls={

        "enabled":

        p.get("security") in [

            "tls",

            "reality"

        ]

    }



    if p.get("sni"):

        tls["server_name"]=p["sni"]





    if p.get("security")=="reality":


        tls["utls"]={

            "enabled":True

        }


        tls["reality"]={

            "enabled":True,


            "public_key":

            p.get("pbk"),



            "short_id":

            p.get("sid","")

        }





    return {

        "type":"vless",

        "server":u.hostname,

        "server_port":u.port,

        "uuid":u.username,

        "tls":tls

    }









def parse_trojan(url):


    u=urlsplit(url)

    p=params(url)



    return {


        "type":"trojan",

        "server":u.hostname,

        "server_port":u.port,

        "password":u.username,

        "tls":{

            "enabled":True,

            "server_name":

            p.get(

                "sni",

                u.hostname

            )

        }

    }









def parse_tuic(url):


    u=urlsplit(url)



    return {


        "type":"tuic",

        "server":u.hostname,

        "server_port":u.port,

        "uuid":u.username,

        "password":u.password,

        "congestion_control":"bbr",


        "tls":{

            "enabled":True

        }

    }









def parse_hysteria2(url):


    u=urlsplit(url)

    p=params(url)



    return {


        "type":"hysteria2",

        "server":u.hostname,

        "server_port":u.port,

        "password":u.username,


        "tls":{

            "enabled":True,

            "server_name":

            p.get(

                "sni",

                u.hostname

            )

        }

    }









def parse_anytls(url):


    u=urlsplit(url)

    p=params(url)



    return {


        "type":"anytls",

        "server":u.hostname,

        "server_port":u.port,

        "password":u.username,


        "tls":{

            "enabled":

            p.get(

                "security"

            )=="tls",

            "server_name":

            p.get(

                "sni",

                u.hostname

            )

        }

    }









def parse_vmess(url):


    raw=url.replace(

        "vmess://",

        ""

    )


    data=base64.b64decode(

        raw+"="*

        (-len(raw)%4)

    )


    obj=json.loads(

        data

    )



    return {


        "type":"vmess",

        "server":

        obj["add"],


        "server_port":

        int(obj["port"]),


        "uuid":

        obj["id"]

    }









def parse_node(url):


    if url.startswith(

        "vless://"

    ):

        return parse_vless(url)



    if url.startswith(

        "trojan://"

    ):

        return parse_trojan(url)



    if url.startswith(

        "tuic://"

    ):

        return parse_tuic(url)



    if (

        url.startswith(

            "hysteria2://"

        )

        or

        url.startswith(

            "hy2://"

        )

    ):

        return parse_hysteria2(url)



    if url.startswith(

        "anytls://"

    ):

        return parse_anytls(url)



    if url.startswith(

        "vmess://"

    ):

        return parse_vmess(url)



    raise ValueError(

        "unsupported protocol"

    )
