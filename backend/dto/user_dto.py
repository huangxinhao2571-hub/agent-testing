from pydantic import BaseModel,Field


class UserRegisterDTO(BaseModel):
    """
    注册接口DTO
    """
    username:str = Field(...,min_length=11,max_length=11,pattern=r"^1[3-9]\d{9}$")
    password:str = Field(...,min_length=6,max_length=10)


class UserLoginDTO(BaseModel):
    """
    登陆接口DTO
    """
    username:str = Field(...,min_length=11,max_length=11,pattern=r"^1[3-9]\d{9}$")
    password:str = Field(...,min_length=6,max_length=10)

