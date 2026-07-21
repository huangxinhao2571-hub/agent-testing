from pydantic import BaseModel,Field


class ProjectCreateDTO(BaseModel):
    """
    创建项目接口dto
    """
    project_name:str = Field(...,min_length=4,max_length=10)
    project_describe:str | None = Field(default=None,max_length=100)
    project_password:str = Field(...,min_length=8,max_length=12)


class ProjectUpdateDTO(BaseModel):
    """
    修改项目接口dto
    """
    project_id: int = Field(..., gt=0)
    project_name:str = Field(...,min_length=4,max_length=10)
    project_describe: str | None = Field(default=None,max_length=100)
    project_password:str = Field(...,min_length=8,max_length=12)


class ProjectDeleteDTO(BaseModel):
    """
    删除项目接口dto
    """
    project_id:int = Field(...,gt=0)



class ProjectListDTO(BaseModel):
    """
    获取项目列表dto
    """
    page:int = Field(default=1,gt=0)
    page_size:int = Field(default=100,gt=0,le=100)
    project_name:str | None = Field(default=None,min_length=4,max_length=10)



# class ProjectSelectDTO(BaseModel):
#     """
#     查询项目dto
#     """
#     page:int = Field(default=1,gt=0)
#     page_size:int = Field(default=100,gt=0,le=100)
#     project_name:str | None = Field(default=None,min_length=4,max_length=10)
#     project_create_name:str = Field(default=None,min_length=1,max_length=10)
