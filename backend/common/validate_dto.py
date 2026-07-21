from pydantic import ValidationError
from backend.common import respones

def validate_dto(dto_class,data):
    """
    封装每个接口service的dto调用函数
    :param dto_class:
    :param data:
    :return:
    """
    try:
        dto = dto_class(**data)
        return dto,None
    except ValidationError as E:
        print(f"参数错误：{E}")
        result = respones.invalid_parameter(
            msg="参数错误",
            data=E.errors()
        )
        return None,result
