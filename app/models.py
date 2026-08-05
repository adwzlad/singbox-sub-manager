from datetime import datetime



from sqlalchemy import (

    Column,

    Integer,

    String,

    Text,

    Boolean,

    DateTime,

    ForeignKey

)



from sqlalchemy.orm import relationship



from app.database import Base







# =========================
# 订阅源
# =========================

class Subscription(Base):


    __tablename__ = "subscriptions"



    id = Column(

        Integer,

        primary_key=True

    )


    name = Column(

        String(128)

    )



    url = Column(

        Text,

        nullable=False

    )


    enabled = Column(

        Boolean,

        default=True

    )


    last_update = Column(

        DateTime

    )





    nodes = relationship(

        "Node",

        back_populates="subscription"

    )









# =========================
# 节点
# =========================

class Node(Base):


    __tablename__ = "nodes"



    id = Column(

        Integer,

        primary_key=True

    )



    subscription_id = Column(

        Integer,

        ForeignKey(

            "subscriptions.id"

        )

    )



    name = Column(

        String(128)

    )



    protocol = Column(

        String(32)

    )



    server = Column(

        String(255)

    )



    port = Column(

        Integer

    )



    outbound = Column(

        Text

    )



    enabled = Column(

        Boolean,

        default=True

    )





    subscription = relationship(

        "Subscription",

        back_populates="nodes"

    )









# =========================
# 模板
# =========================

class Template(Base):


    __tablename__="templates"



    id = Column(

        Integer,

        primary_key=True

    )



    name = Column(

        String(128)

    )



    version = Column(

        String(32),

        default="1"

    )



    content = Column(

        Text,

        nullable=False

    )



    enabled = Column(

        Boolean,

        default=True

    )









# =========================
# Hosts
# =========================

class Host(Base):


    __tablename__="hosts"



    id = Column(

        Integer,

        primary_key=True

    )



    domain = Column(

        String(255)

    )



    ip = Column(

        String(64)

    )



    enabled = Column(

        Boolean,

        default=True

    )









# =========================
# 生成配置记录
# =========================

class Config(Base):


    __tablename__="configs"



    id = Column(

        Integer,

        primary_key=True

    )



    name = Column(

        String(128)

    )



    template_id = Column(

        Integer

    )



    file_path = Column(

        Text

    )



    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )









# =========================
# 订阅Token
# =========================

class SubscriptionToken(Base):


    __tablename__="subscription_tokens"



    id = Column(

        Integer,

        primary_key=True

    )



    name = Column(

        String(128)

    )



    token_hash = Column(

        String(64),

        unique=True,

        nullable=False

    )



    enabled = Column(

        Boolean,

        default=True

    )



    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )
