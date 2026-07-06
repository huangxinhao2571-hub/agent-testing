from backend.extensions import db


def verify_user_id(user_id):
    """
    全局拦截器verify_token，用户态校验：
    1、根据token中的user_id校验用户是否存在
    2、校验用户的status是否为1（正常）
    :param user_id:
    :return:
    """
    sql = "SELECT username,role,status FROM users WHERE user_id = %s"
    result = db.db_fetchone(sql,[user_id])
    return result