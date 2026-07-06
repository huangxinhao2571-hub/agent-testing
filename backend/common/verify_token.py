from flask import request,g
from backend.config import DevConfig
from backend.common import respones,jwt_utils
from backend.repositories import verify
import jwt

def verify_token():
    """
    作用1: 全局鉴权拦截器
    如果请求接口不是登陆和注册，统一校验token

    作用2: 将token解码后的payload存入g对象中，供后续接口使用:如user_id
    :return:
    """

    # 校验是否是白名单接口
    if request.path in DevConfig.AUTH_WHITELIST:
        return

    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        return respones.invalid_parameter(msg="鉴权失败")


    token = auth_header.split(" ")[1]

    try:
        payload = jwt_utils.verify_token(token)
        user_id = payload.get("user_id")

        # 校验用户是否存在
        user_info = verify.verify_user_id(user_id)
        if not user_info:
            return respones.unauthorized()

        # 校验用户status是否为1
        db_username, db_role, db_status = user_info
        if db_status != 1:
            return respones.forbidden(msg="用户状态异常")

        g.payload = payload
        return

    except jwt.ExpiredSignatureError:
        print("token已过期")
        return respones.unauthorized(msg="token已过期")
    except jwt.InvalidAudienceError:
        print("aud不匹配")
        return respones.unauthorized(msg="aud不匹配")
    except jwt.InvalidIssuerError:
        print("iss不匹配")
        return respones.unauthorized(msg="iss不匹配")
    except jwt.InvalidSignatureError:
        print("token签名无效")
        return respones.unauthorized(msg="token签名无效")
    except jwt.DecodeError:
        print("token格式错误")
        return respones.unauthorized(msg="token格式错误")
    except jwt.InvalidTokenError:
        print("token非法")
        return respones.unauthorized(msg="token非法")
