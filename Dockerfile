FROM python:3.12-slim


WORKDIR /app



# =========================
# 安装Python依赖
# 单独一层，方便缓存
# =========================

COPY requirements.txt .


RUN pip install --no-cache-dir \
    -r requirements.txt





# =========================
# 复制项目代码
# 修改代码只影响这一层
# =========================

COPY app ./app

COPY web ./web





# =========================
# 创建数据目录
# =========================

RUN mkdir -p /data





ENV DATA_DIR=/data



EXPOSE 8000





CMD [

"uvicorn",

"app.main:app",

"--host",

"0.0.0.0",

"--port",

"8000"

]
