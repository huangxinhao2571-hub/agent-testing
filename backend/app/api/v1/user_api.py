from flask import Blueprint,request
from backend.services import user_service

user_api_bp = Blueprint("user_api_bp",__name__)

@user_api_bp.route("/register",methods=["POST"])
def register():
    """
    注册接口 --蓝图
        接收用户参数
        调用service业务模块

    :return: service模块返回接口对应响应
    """
    user_info = request.get_json(silent=True) or {}
    result = user_service.service_register(user_info)
    return result




@user_api_bp.route("/login",methods=["POST"])
def login():
    user_info = request.get_json(silent=True) or {}
    result = user_service.service_login(user_info)
    return result




