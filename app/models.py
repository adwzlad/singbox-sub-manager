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


from datetime import datetime



from app.database import Base







# =========================
# 订阅源
# =========================

class Subscription(Base):


    __tablename__ = "subscriptions"



    id = Column(

        Integer,

        primary_key=True,

        index=True

    )


    name = Column(

        String(128),

        nullable=False

    )


    url = Column(

        Text,

        nullable=False

    )


    enabled = Column(

        Boolean,

        default=True

    )


    update_interval = Column(

        Integer,

        default=3600

    )


    last_update = Column(

        DateTime

    )


    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )



    nodes = relationship(

        "Node",

        back_populates="subscription",

        cascade="all, delete"

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


    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )



    subscription = relationship(

        "Subscription",

        back_populates="nodes"

    )









# =========================
# sing-box模板
# =========================

class Template(Base):


    __tablename__ = "templates"



    id = Column(

        Integer,

        primary_key=True

    )


    name = Column(

        String(128),

        nullable=False

    )


    version = Column(

        String(32),

        default="1.0"

    )


    content = Column(

        Text,

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









# =========================
# Hosts映射
# =========================

class Host(Base):


    __tablename__ = "hosts"



    id = Column(

        Integer,

        primary_key=True

    )


    domain = Column(

        String(255),

        unique=True,

        index=True

    )


    ip = Column(

        String(128)

    )


    enabled = Column(

        Boolean,

        default=True

    )


    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )









# =========================
# 生成配置记录
# =========================

class Config(Base):


    __tablename__ = "configs"



    id = Column(

        Integer,

        primary_key=True

    )


    name = Column(

        String(128)

    )


    template_id = Column(

        Integer,

        ForeignKey(

            "templates.id"

        )

    )


    file_path = Column(

        Text

    )


    version = Column(

        Integer,

        default=1

    )


    active = Column(

        Boolean,

        default=True

    )


    created_at = Column(

        DateTime,

        default=datetime.utcnow

    )


    template = relationship(

        "Template"

    )
