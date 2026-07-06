from http import HTTPStatus
from flask import jsonify


# HTTPStatus 常用状态码说明：
# HTTPStatus.OK = 200，请求成功，常用于查询、修改、删除成功
# HTTPStatus.CREATED = 201，资源创建成功，常用于新增数据成功
# HTTPStatus.NO_CONTENT = 204，请求成功但无响应体，常用于删除成功且不返回 data
#
# HTTPStatus.MOVED_PERMANENTLY = 301，永久重定向
# HTTPStatus.FOUND = 302，临时重定向
# HTTPStatus.NOT_MODIFIED = 304，资源未变化，浏览器可使用缓存
#
# HTTPStatus.BAD_REQUEST = 400，请求参数错误、参数缺失、JSON 格式错误
# HTTPStatus.UNAUTHORIZED = 401，未登录、token 缺失、token 无效或 token 过期
# HTTPStatus.FORBIDDEN = 403，已登录但没有权限访问或操作
# HTTPStatus.NOT_FOUND = 404，请求的接口或资源不存在
# HTTPStatus.METHOD_NOT_ALLOWED = 405，请求方法不允许，例如接口只支持 POST 却用了 GET
# HTTPStatus.CONFLICT = 409，资源冲突，例如用户名已存在、项目名重复
# HTTPStatus.UNPROCESSABLE_ENTITY = 422，请求格式正确，但业务规则校验不通过
# HTTPStatus.TOO_MANY_REQUESTS = 429，请求过于频繁，被限流
#
# HTTPStatus.INTERNAL_SERVER_ERROR = 500，服务端未知异常
# HTTPStatus.BAD_GATEWAY = 502，网关或上游服务异常
# HTTPStatus.SERVICE_UNAVAILABLE = 503，服务暂不可用，例如维护中或依赖服务不可用
# HTTPStatus.GATEWAY_TIMEOUT = 504，网关或上游服务超时


SUCCESS_CODE = 0
MISSING_PARAMETER_CODE = 40001
INVALID_PARAMETER_CODE = 40002
UNAUTHORIZED_CODE = 40100
FORBIDDEN_CODE = 40300
NOT_FOUND_CODE = 40400
UNKNOWN_ERROR_CODE = 50000
CUSTOM_ERROR_CODE = 50001


def common_response(
    status: bool,
    msg: str,
    data=None,
    code: int = SUCCESS_CODE,
    http_status: int = HTTPStatus.OK,
):
    """
    统一接口响应结构。

    :param status: 业务处理是否成功
    :param msg: 响应提示信息
    :param data: 响应数据，默认空字典
    :param code: 业务状态码，0 表示成功
    :param http_status: HTTP 状态码
    :return: Flask JSON 响应
    """
    if data is None:
        data = {}

    result = {
        "status": status,
        "code": code,
        "msg": msg,
        "data": data,
    }
    return jsonify(result), http_status


def success(msg="成功", data=None):
    """
    请求成功。
    """
    return common_response(
        status=True,
        code=SUCCESS_CODE,
        msg=msg,
        data=data,
        http_status=HTTPStatus.OK,
    )


def missing_parameter(msg="参数缺失", data=None):
    """
    必填参数缺失。
    """
    return common_response(
        status=False,
        code=MISSING_PARAMETER_CODE,
        msg=msg,
        data=data,
        http_status=HTTPStatus.BAD_REQUEST,
    )


def invalid_parameter(msg="参数错误", data=None):
    """
    参数格式错误或业务参数不合法。
    """
    return common_response(
        status=False,
        code=INVALID_PARAMETER_CODE,
        msg=msg,
        data=data,
        http_status=HTTPStatus.BAD_REQUEST,
    )


def unauthorized(msg="鉴权失败", data=None):
    """
    未登录、token 无效或 token 过期。
    """
    return common_response(
        status=False,
        code=UNAUTHORIZED_CODE,
        msg=msg,
        data=data,
        http_status=HTTPStatus.UNAUTHORIZED,
    )


def forbidden(msg="无权限操作", data=None):
    """
    已登录，但没有操作权限。
    """
    return common_response(
        status=False,
        code=FORBIDDEN_CODE,
        msg=msg,
        data=data,
        http_status=HTTPStatus.FORBIDDEN,
    )


def not_found(msg="资源不存在", data=None):
    """
    查询的资源不存在。
    """
    return common_response(
        status=False,
        code=NOT_FOUND_CODE,
        msg=msg,
        data=data,
        http_status=HTTPStatus.NOT_FOUND,
    )


def unknown_error(msg="未知异常", data=None):
    """
    服务端未知异常。
    """
    return common_response(
        status=False,
        code=UNKNOWN_ERROR_CODE,
        msg=msg,
        data=data,
        http_status=HTTPStatus.INTERNAL_SERVER_ERROR,
    )


def custom_error(msg="自定义异常", data=None, code=CUSTOM_ERROR_CODE, http_status=HTTPStatus.BAD_REQUEST):
    """
    自定义错误响应。
    """
    return common_response(
        status=False,
        code=code,
        msg=msg,
        data=data,
        http_status=http_status,
    )
