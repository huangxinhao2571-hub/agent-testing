
from flask import Blueprint,request
from backend.services import case_service

case_api_bp = Blueprint("case_api_bp",__name__)

@case_api_bp.route("/upload",methods=["POST"])
def upload():
    """
    用户上传接口
    :return: {文件名：文件名，文件路径：文件路径}
    """
    file = request.files.get("requirement_file")  # requirement_file是和前端约束好的文件的key
    result =  case_service.service_upload(file)
    return result


@case_api_bp.route("/function_point",methods=["POST"])
def function_point():
    """
    1、根据前端传的文件id（文件路径），得到文件内容
    2、通过文件内容来对各个模块和各个功能点进行分块
    :return: [模块名：模块名，功能名：功能名，功能点：功能点]
    """
    file_id = request.json.get("file_id")

