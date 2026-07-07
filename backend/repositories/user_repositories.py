from backend.extensions import db


def create_user(username,password,user_id):
    """
    注册接口校验通过
        将用户信息存入数据库
        执行inset语句
    :param username: 账号
    :param password: 密码
    :return: 返回成功或失败：1或者0
    """
    sql = "insert into users (username,password,role,user_id) values (%s,%s,0,%s)"
    return db.db_execute(sql,[username,password,user_id])


def get_user_by_username(username):
    """
    注册需要查询users库中用户名是否重复
    :param username: 用户名
    :return: 如果查询到数据用户名重复/如果为None，就说明不重复
    """
    sql = "select * from users where username = %s"
    return db.db_fetchone(sql,[username])


def get_userinfo_by_username(username):
    """
    登陆时，通过账号查询密码，在services中进行比对
    :param username: 用户名
    :return: 返回对应用户名的密码
    """
    sql = "select username,password,role,user_id,status from users where username = %s"
    return db.db_fetchone(sql,[username])
