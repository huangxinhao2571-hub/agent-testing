import re
from backend.common import respones,jwt_utils,create_id
from backend.repositories import user_repositories
from backend.dto import user_dto
from pydantic import ValidationError

def service_register(user_info):
    """
    注册 接口的业务逻辑处理
      数据校验
      json数据返回

    :param user_info: 前端传入的注册 JSON 数据，包含 username、password
    :return:返回接口对应响应：成功 or 失败
    """
    try:
        dto = user_dto.UserRegisterDTO(**user_info)
    except ValidationError as E:
        print(f"参数错误：{E}")
        return respones.invalid_parameter(
            msg="参数错误",
            data=E.errors()
        )

    username = dto.username
    password = dto.password

    if user_repositories.get_user_by_username(username):
        return respones.invalid_parameter(msg="用户名已存在")

    user_id = create_id.create_id()

    # 添加账号密码入库
    try:
        result = user_repositories.create_user(username,password,user_id)
        if not result:
            return respones.unknown_error(msg="注册失败")

    except Exception as E:
        print(f"注册用户入库失败：{E}")
        return respones.unknown_error(msg="注册失败")


    else:
        # 返回注册接口json响应
        return respones.success(
            msg="注册成功",
            data={
                "username":username,
                "password":password,
                "role":0
            }
        )




def service_login(user_info):
    """
    登录 接口的业务逻辑处理
      数据校验
      登录校验
      token生成
      json数据返回

    :param user_info:前端传入的注册 JSON 数据，包含 username、password
    :return:返回接口对应响应：成功 or 失败
    """
    # 登陆参数校验
    try:
        dto = user_dto.UserLoginDTO(**user_info)
    except ValidationError as E:
        print(f"参数错误{E}")
        return respones.invalid_parameter(
            msg="参数错误",
            data=E.errors()
        )

    username = dto.username
    password = dto.password


    # 业务逻辑校验
    user = user_repositories.get_userinfo_by_username(username)
    if not user:
        return respones.invalid_parameter(msg="用户未注册")

    # 查询数据库中的用户名、密码、角色、user_id、状态
    db_user_info = user_repositories.get_userinfo_by_username(username)
    db_username,db_password,db_role,db_user_id,db_status = db_user_info
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






