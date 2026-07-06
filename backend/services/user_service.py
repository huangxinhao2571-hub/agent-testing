import re
from backend.common import respones,jwt_utils,create_id
from backend.repositories import user_repositories

def service_register(username,password,role=0):
    """
    注册 接口的业务逻辑处理
      数据校验
      json数据返回

    :param username:手机号
    :param password:密码
    :param role:用户角色
    :return:返回接口对应响应：成功 or 失败
    """

    # 注册参数校验
    if not username or not password:
        return respones.missing_parameter(msg="账号密码不允许为空")

    if len(username) != 11 or len(password) < 6 or len(password) > 10:
        return respones.invalid_parameter(msg="请输入正确格式账号密码")

    if user_repositories.get_user_by_username(username):
        return respones.invalid_parameter(msg="用户名已存在")


    username = username.strip()
    if not re.match(r"^1[3-9]\d{9}$", username):
        return respones.invalid_parameter(msg="手机号格式不正确")


    user_id = create_id.create_id()



    # 添加账号密码入库
    try:
        result = user_repositories.create_user(username,password,role,user_id,)
        if not result:
            return respones.unknown_error(msg="注册失败")

    except Exception as E:
        print(f"注册用户入库失败：{E}")
        return respones.unknown_error(msg="注册失败")


    else:
        # 返回注册接口json响应
        return respones.success(msg="注册成功", data={})




def service_login(username,password):
    """
    登录 接口的业务逻辑处理
      数据校验
      登录校验
      token生成
      json数据返回

    :param username:手机号
    :param password:密码
    :return:返回接口对应响应：成功 or 失败
    """
    # 登陆参数校验
    if not username or not password:
        return respones.missing_parameter(msg="账号密码不允许为空")

    if len(username) != 11 or len(password) < 6 or len(password) > 10:
        return respones.invalid_parameter(msg="请输入正确格式账号密码")

    username = username.strip()
    if not re.match(r"^1[3-9]\d{9}$", username):
        return respones.invalid_parameter(msg="手机号格式不正确")


    # 业务逻辑校验
    user = user_repositories.get_userinfo_by_username(username)
    if not user:
        return respones.invalid_parameter(msg="用户未注册")

    # 查询数据库中的用户名、密码、角色、user_id、状态
    user_info = user_repositories.get_userinfo_by_username(username)
    db_username,db_password,db_role,db_user_id,db_status = user_info
    print(db_username,db_password,db_role,db_user_id,db_status)

    # 校验数据库中的密码是否正确
    if db_password != password:
        return respones.invalid_parameter("账号或密码错误")


    # 校验数据库中的用户的状态是否正常
    if db_status != 1:
        return respones.forbidden(msg="用户状态异常")




    # 登录成功后，生成jwt token
    try:
        jwt_token = jwt_utils.generate_token(db_username,db_role,db_user_id)
        return respones.success(data={"token":jwt_token})
    except Exception as E:
        print(f"生成jwt_token失败:{E}")
        return respones.custom_error(msg=f"生成jwt_token失败：{E}")






