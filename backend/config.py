import os


class DevConfig:
    # PostgreSQL
    DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
    DB_PORT = int(os.getenv("DB_PORT", 5432))
    DB_USER = os.getenv("DB_USER", "gebilaohuang")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "123456")
    DB_NAME = os.getenv("DB_NAME", "postgres")

    # Redis
    REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")
    REDIS_DB = int(os.getenv("REDIS_DB", 0))


    # Token鉴权的JWT(json_web_token)变量
    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY",
        "flask-teamhelper-dev-secret-key-2026"
    )
    JWT_ISS = os.getenv("JWT_ISS","flask-teamhelper")
    JWT_AUD = os.getenv("JWT_AUD","teamhelper-web")


    # 鉴权校验白名单列表
    AUTH_WHITELIST = os.getenv("AUTH_WHITELIST",["/api/v1/user/login", "/api/v1/user/register"])
