from unittest import result

from backend.extensions import db

def create_project(project_name: str, project_describe: str, project_password: str,project_creator_id):
    """
    执行创建项目sql
    :param project_name:
    :param project_describe:
    :param project_password:
    :return:
    """
    sql = """
        INSERT INTO projects (
            project_name,
            project_describe,
            project_password,
            project_creator_id
        ) VALUES (%s,%s,%s,%s)
            returning project_id
    """
    result = db.db_execute_returning_one(sql,[project_name,project_describe,project_password,project_creator_id])
    return result


def check_project_permission(project_id):
    """
    项目操作权限校验
    1、项目是否存在
    2、操作人 是否 = 项目创建人
    :param project_creator_id: 项目创建人
    :param project_id: 项目id
    :return:
    """
    sql = """
    SELECT project_creator_id , project_status FROM projects WHERE project_id = %s
    """

    result = db.db_fetchone(sql,[project_id])
    return result


def update_project(project_name: str, project_describe: str, project_password: str, project_id: int):
    """
    执行修改项目sql
    :param project_name:
    :param project_describe:
    :param project_password:
    :param project_id:
    :return:
    """
    sql = """
    UPDATE projects SET 
    project_name = %s, 
    project_describe = %s, 
    project_password = %s 
    WHERE project_id = %s
    """
    result = db.db_execute(sql,[project_name,project_describe,project_password,project_id])
    return result


def delete_project(project_id):
    """
    执行软删除项目，本质就是把project_status状态改成0
    :param project_id:
    :return:
    """
    sql = """
    UPDATE projects SET 
    project_status = '0' 
    WHERE project_id = %s
    """
    result = db.db_execute(sql,[project_id])
    return result


def list_projects_by_creator(project_creator_id,page,page_size,project_name=None):
    """
    1、执行查询项目列表，根据user_id查询该账号所有状态正常的项目
    2、动态校验projectname，校验是搜索还是全局查，动态sql
    :param project_creator_id:
    :param page:
    :param page_size:
    :return:
    """
    offset = (page - 1) * page_size # offset是算出跳过多少条

    sql = """
        SELECT project_id,project_name,project_describe,updated_at,project_status 
        FROM projects 
        WHERE project_creator_id = %s 
          AND project_status = '1' 
    """
    param = [project_creator_id]

    if project_name:
        sql += " AND project_name like %s"
        param.append(f"%{project_name}%")

    sql += """
        ORDER BY created_at 
        DESC LIMIT %s OFFSET %s
    """
    param.extend([page_size,offset])

    result = db.db_fetchall_dict(sql,param)
    return result