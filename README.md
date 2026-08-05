# singbox-sub-manager


## 项目简介

singbox-sub-manager 是一个基于 Docker 部署的 sing-box 订阅管理工具。

用于：

- 管理 sing-box 节点订阅
- 生成 sing-box 配置文件
- 管理 Hosts 替换
- 提供订阅地址给 sing-box 客户端使用



---

# 部署方法


## 1. 获取项目


```bash
git clone https://github.com/yourname/singbox-sub-manager.git

cd singbox-sub-manager

2. 修改配置

编辑：

docker-compose.yml

修改：

ADMIN_KEY: your-password

例如：

ADMIN_KEY: abc123456

ADMIN_KEY 用于管理后台验证，请自行修改。

3. 启动服务

首次启动：

docker compose up -d --build

查看运行状态：

docker ps

查看日志：

docker logs singbox-sub-manager
使用方法
Web管理页面

浏览器访问：

http://服务器IP:8000/web/index.html

输入：

ADMIN_KEY

即可进入管理操作。

数据目录

默认数据保存在：

data/

结构：

data/

├── app.db

└── configs/


其中：

app.db 保存数据库
configs 保存生成的 sing-box 配置文件

删除容器不会影响数据。

停止服务

停止：

docker compose down

重新启动：

docker compose up -d
更新项目

拉取最新代码：

git pull

重新构建：

docker compose up -d --build

已有数据不会丢失。

备份

备份：

cp -r data data_backup

恢复：

cp -r data_backup data
默认端口

Web服务：

8000

访问：

http://服务器IP:8000
