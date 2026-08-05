import base64

import json

import urllib.parse







def parse_params(url):

    return dict(

        urllib.parse.parse_qsl(

            urllib.parse.urlsplit(url).query

        )

    )









# =========================
# VLESS
# =========================

def parse_vless(url):


    u = urllib.parse.urlsplit(url)


    params = parse_params(url)



    return {


        "type": "vless",


        "server": u.hostname,


        "server_port": u.port,


        "uuid": u.username,



        "tls": {


            "enabled":

            params.get(

                "security"

            ) in [

                "tls",

                "reality"

            ],



            "server_name":

            params.get(

                "sni",

                u.hostname

            )

        }

    }









# =========================
# VMess
# =========================

def parse_vmess(url):


    data=url.replace(

        "vmess://",

        ""

    )



    raw=base64.b64decode(

        data +

        "=" *

        (-len(data)%4)

    )



    obj=json.loads(

        raw.decode()

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









# =========================
# Trojan
# =========================

def parse_trojan(url):


    u=urllib.parse.urlsplit(url)


    params=parse_params(url)



    return {


        "type":"trojan",


        "server":

        u.hostname,



        "server_port":

        u.port,



        "password":

        u.username,



        "tls":{


            "enabled":True,


            "server_name":

            params.get(

                "sni",

                u.hostname

            )

        }

    }









# =========================
# TUIC
# =========================

def parse_tuic(url):


    u=urllib.parse.urlsplit(url)


    params=parse_params(url)



    return {


        "type":"tuic",


        "server":

        u.hostname,



        "server_port":

        u.port,



        "uuid":

        u.username,



        "password":

        u.password,



        "tls":{


            "enabled":True,


            "server_name":

            params.get(

                "sni",

                u.hostname

            )

        }

    }









# =========================
# Hysteria2
# =========================

def parse_hysteria2(url):


    u=urllib.parse.urlsplit(url)


    params=parse_params(url)



    return {


        "type":"hysteria2",


        "server":

        u.hostname,



        "server_port":

        u.port,



        "password":

        u.username,



        "tls":{


            "enabled":True,


            "server_name":

            params.get(

                "sni",

                u.hostname

            )

        }

    }









# =========================
# AnyTLS
# =========================

def parse_anytls(url):


    u=urllib.parse.urlsplit(url)


    params=parse_params(url)



    return {


        "type":"anytls",


        "server":

        u.hostname,



        "server_port":

        u.port,



        "password":

        u.username,



        "tls":{


            "enabled":

            params.get(

                "security"

            )=="tls",



            "server_name":

            params.get(

                "sni",

                u.hostname

            )

        }

    }









# =========================
# Shadowsocks
# =========================

def parse_ss(url):


    data=url.replace(

        "ss://",

        ""

    )



    data=data.split("#")[0]



    raw=base64.b64decode(

        data +

        "=" *

        (-len(data)%4)

    ).decode()



    method_pwd,server=raw.rsplit(

        "@",

        1

    )



    method,password=method_pwd.split(

        ":",

        1

    )



    host,port=server.split(

        ":"

    )



    return {


        "type":"shadowsocks",


        "server":host,


        "server_port":int(port),


        "method":method,


        "password":password

    }









# =========================
# 主入口
# =========================

def parse_node(url):


    url=url.strip()



    if url.startswith("vless://"):

        return parse_vless(url)



    if url.startswith("vmess://"):

        return parse_vmess(url)



    if url.startswith("trojan://"):

        return parse_trojan(url)



    if url.startswith("tuic://"):

        return parse_tuic(url)



    if (

        url.startswith("hysteria2://")

        or

        url.startswith("hy2://")

    ):

        return parse_hysteria2(url)



    if url.startswith("anytls://"):

        return parse_anytls(url)



    if url.startswith("ss://"):

        return parse_ss(url)



    raise ValueError(

        "Unsupported node protocol"

    )
