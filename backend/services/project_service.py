from backend.common import respones
from backend.repositories import project_repositories


def check_project(project_id,project_creator_id):
    """
    项目模块公共校验方法
    1、校验项目id是否存在
    2、校验项目的status是否为1
    3、校验项目创建人是否等于当前操作人
    :param project_id:
    :param project_creator_id:
    :return:
    """
    try:
        # 先校验project_id是否存在，project_status是否为1，以及project_creator_id人是否有权限
        project_info = project_repositories.check_project_permission(project_id)

    except Exception as E:
        print(f"校验项目信息失败：{E}")
        return respones.unknown_error(msg="校验项目信息失败")

    else:
        if project_info is None:
            return respones.not_found(msg="项目不存在")

        db_project_creator_id,db_project_status = project_info

        if db_project_status != 1:
            return respones.not_found(msg="项目不存在")

        if str(db_project_creator_id) != str(project_creator_id):
            return respones.forbidden(msg="无权限操作")
        # 为了service调用做判断，None就代表校验通过
        return None




def service_create(data,project_creator_id):
        """
        创建应用service层实现方法
        :param project_name:
        :param project_describe:
        :param project_password:
        :return:
        """
        project_name = data.get("project_name")
        project_describe = data.get("project_describe")
        project_password = data.get("project_password")


        # 参数缺失校验
        if not project_name or not project_describe or not project_password:
            return respones.missing_parameter(msg="参数不能为空")

        if len(project_name) > 10 or len(project_describe) > 100 or len(project_password) > 8:
            return respones.invalid_parameter(msg="项目名称最多10位，描述最多100位，密码最多8位")

        try:
            # 将项目信息写入数据库
            result = project_repositories.create_project(project_name, project_describe, project_password,project_creator_id)
            if not result:
                return respones.unknown_error(msg="创建项目失败")

        except Exception as E:
            print(f"创建项目入库失败：{E}")
            return respones.unknown_error(msg="创建项目失败")

        else:
            project_id = result[0]
            return respones.success(
                msg="创建成功",
                data={
                    "project_id": project_id,
                    "project_name": project_name,
                    "project_describe": project_describe,
                }
            )



def service_update(data,project_creator_id):
    """
    修改项目的service实现方法
    :param data: 获取前端传参json
    :param project_creator_id: 获取token解析的user_id
    :return:
    """
    # 获取前端请求中传的project_id
    project_id = data.get("project_id")

    project_name = data.get("project_name")
    project_describe = data.get("project_describe")
    project_password = data.get("project_password")



    # 参数缺失校验
    required_fields = ["project_name", "project_describe", "project_password", "project_id"]

    for field in required_fields:
        if not data.get(field):
            return respones.missing_parameter(msg=f"{field}不能为空")

    if len(project_name) > 10 or len(project_describe) > 100 or len(project_password) > 8:
        return respones.invalid_parameter(msg="项目名称最多10位，描述最多100位，密码最多8位")

    # 执行项目公共校验
    error = check_project(project_id,project_creator_id)

    if error:
        return error

    try:
        # 执行修改sql
        result = project_repositories.update_project(project_name, project_describe, project_password,project_id)
        if not result:
            return respones.unknown_error("修改项目失败")

    except Exception as E:
        print(f"修改项目入库失败：{E}")
        return respones.unknown_error("修改项目失败")

    else:
        return respones.success(
            msg="修改成功",
            data={
                "project_id": project_id,
                "project_name": project_name,
                "project_describe": project_describe,
            }
        )


def service_delete(data,project_creator_id):
    """
    删除项目的service实现方法
    :param data:
    :param project_creator_id:
    :return:
    """
    # 获取前端请求中传的project_id
    project_id = data.get("project_id")

    if not project_id:
        return respones.missing_parameter("参数为空")

    # 执行项目公共校验
    error = check_project(project_id,project_creator_id)

    if error:
        return error

    try:
        result = project_repositories.delete_project(project_id)
        if not result:
            return respones.unknown_error("删除项目失败")
    except Exception as E:
        print(f"数据库删除项目执行失败：{E}")
        return respones.unknown_error("删除项目失败")
    else:
        return respones.success(
            msg="删除成功",
            data={
                "project_id":project_id
            }
        )









