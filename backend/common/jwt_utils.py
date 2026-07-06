import jwt
from datetime import datetime,timezone,timedelta
import uuid
from backend.config import DevConfig


def generate_token(username,role,user_id):
    """
    生成 jwt_token
        登录成功后，生成对应用户的jwt token
        将用户名、角色、user_id 签发信息保存到payload中

    :param username: 用户名
    :param role: 用户角色
    :return: 返回生成好的jwt token字符串
    """
    payload = {
        "username":username,
        "role":role,
        "user_id":user_id,
        "iss":DevConfig.JWT_ISS,
        "aud":DevConfig.JWT_AUD,
        "iat":datetime.now(timezone.utc),
        "exp":datetime.now(timezone.utc) + timedelta(days=2),
        "jti":str(uuid.uuid4())
    }
    token = jwt.encode(payload,DevConfig.JWT_SECRET_KEY,algorithm="HS256")
    return token



def verify_token(token):
    """
    校验 jwt_token
        对前端传递过来的jwt token进行解析和校验
        校验成功后，返回payload中的用户信息

    :param token: 前端请求头中携带的jwt token
    :return: 返回解析后的payload数据
    """
    pay_load = jwt.decode(
        token,
        DevConfig.JWT_SECRET_KEY,
        algorithms=["HS256"],
        audience=DevConfig.JWT_AUD,
        issuer=DevConfig.JWT_ISS,
    )
    return pay_load
