from backend.common import respones
from backend.common.validate_dto import validate_dto
from backend.repositories import project_repositories
from backend.dto import project_dto



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
        db_project_info = project_repositories.check_project_permission(project_id)

    except Exception as E:
        print(f"校验项目信息失败：{E}")
        return respones.unknown_error(msg="校验项目信息失败")

    else:
        if db_project_info is None:
            return respones.not_found(msg="项目不存在")

        db_project_creator_id,db_project_status = db_project_info

        if db_project_status != 1:
            return respones.not_found(msg="项目不存在")

        if str(db_project_creator_id) != str(project_creator_id):
            return respones.forbidden(msg="无权限操作")
        # 为了service调用做判断，None就代表校验通过
        return None




def service_create(project_info,project_creator_id):
        """
        创建应用service层实现方法
        :param project_info:
        :param project_creator_id:
        :return:
        """

        # dto参数校验
        dto,error = validate_dto(project_dto.ProjectCreateDTO,project_info)
        if error:
            return error

        project_name = dto.project_name
        project_describe = dto.project_describe
        project_password = dto.project_passwords


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



def service_update(project_info,project_creator_id):
    """
    修改项目的service实现方法
    :param data: 获取前端传参json
    :param project_creator_id: 获取token解析的user_id
    :return:
    """
    # dto参数校验
    dto,dto_error = validate_dto(project_dto.ProjectUpdateDTO,project_info)
    if dto_error:
        return dto_error

    project_id = dto.project_id
    project_name = dto.project_name
    project_describe = dto.project_describe
    project_password = dto.project_password


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


def service_delete(project_info,project_creator_id):
    """
    删除项目的service实现方法
    :param data:
    :param project_creator_id:
    :return:
    """
    # dto参数校验
    dto,dto_error = validate_dto(project_dto.ProjectDeleteDTO,project_info)
    if dto_error:
        return dto_error

    project_id = dto.project_id

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

def service_list(project_info,project_creator_id):
    """
    1、查询项目列表
    2、根据项目名称搜索，通过动态sql绑定成一个接口
    :param project_info:
    :param project_creator_id:
    :return:
    """
    dto,dto_error = validate_dto(project_dto.ProjectListDTO,project_info)
    if dto_error:
        return dto_error

    page = dto.page
    page_size = dto.page_size
    project_name = dto.project_name

    try:
        result = project_repositories.list_projects_by_creator(project_creator_id,page,page_size,project_name)
    except Exception as E:
        print(f"数据库查询项目列表失败：{E}")
        return respones.unknown_error(msg="查询列表失败")
    else:
        return respones.success(
            msg="查询列表成功",
            data=result
        )











