from flask import Blueprint,request,g
from backend.services import project_service


project_api_bp = Blueprint("project_api_bp",__name__)


@project_api_bp.route("/create",methods=["POST"])
def create():
    """
    蓝图 --创建项目模块
    创建项目接口
    :return:
    """
    project_info = request.get_json(silent=True) or {}
    project_creator_id = g.payload.get("user_id")
    result = project_service.service_create(project_info,project_creator_id)
    return result







@project_api_bp.route("/update",methods=["PUT"])
def update():
    """
    修改项目接口
    :return:
    """
    project_info = request.get_json(silent=True) or {}
    project_creator_id = g.payload.get("user_id")
    result = project_service.service_update(project_info,project_creator_id)
    return result




@project_api_bp.route("/delete",methods=["DELETE"])
def delete():
    """
    删除项目接口
    :return:
    """
    project_info = request.get_json(silent=True) or {}
    project_creator_id = g.payload.get("user_id")
    result = project_service.service_delete(project_info,project_creator_id)
    return result





@project_api_bp.route("/project_list",methods=["GET"])
def project_list():
    """
    获取项目列表信息接口
    :return:
    """
    project_params = request.args.to_dict()
    project_creator_id = g.payload.get("user_id")
    result = project_service.service_list(project_params,project_creator_id)
    return result




