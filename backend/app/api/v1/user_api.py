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
    username = request.json.get("username")
    password = request.json.get("password")
    role = request.json.get("role")

    result = user_service.service_register(username,password,role)
    return result




@user_api_bp.route("/login",methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    result = user_service.service_login(username,password)
    return result




