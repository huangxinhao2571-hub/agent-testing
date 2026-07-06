import jwt
from backend.common import respones,jwt_utils
from flask import request
from functools import wraps

# 校验token装饰器
def login_required(func):
    @wraps(func)   # 为了让api接口函数名，保留原来的名字，不然都变成了wrapper，路由就会报错
    def wrapper(*args,**kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return respones.invalid_parameter(msg="鉴权失败")


        token = auth_header.split(" ")[1]

        try:
            jwt_utils.verify_token(token)
        except jwt.ExpiredSignatureError:
            print("token已过期")
            return respones.invalid_parameter(msg="token已过期")
        except jwt.InvalidAudienceError:
            print("aud不匹配")
            return respones.invalid_parameter(msg="aud不匹配")
        except jwt.InvalidIssuerError:
            print("iss不匹配")
            return respones.invalid_parameter(msg="iss不匹配")
        except jwt.InvalidSignatureError:
            print("token签名无效")
            return respones.invalid_parameter(msg="token签名无效")
        except jwt.DecodeError:
            print("token格式错误")
            return respones.invalid_parameter(msg="token格式错误")
        except jwt.InvalidTokenError:
            print("token非法")
            return respones.invalid_parameter(msg="token非法")

        return func(*args,**kwargs)

    return wrapper

