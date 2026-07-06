# from backend.common import respones
# from pathlib import Path
# from langchain
#
# FILE_TYPE = [".txt",".pdf",".md"]
# FILE_PATH = "../upload/files"
#
# def service_upload(file):
#     """
#     文件上传的service业务实现层
#     :param file: 实际上传的file对象
#     :return:
#     """
#     if not file:
#         return respones.missing_parameter(msg="请上传文件")
#
#     if file.name == "":
#         return respones.missing_parameter(msg="文件名不能为空")
#
#     file_type = Path(file.name).suffix  # 查看文件的后缀格式 .txt
#     print(file_type)
#
#     if file_type not in FILE_TYPE:
#         return respones.invalid_parameter(msg="暂不支持该文件类型")
#
#     # parents=True：自动创建父目录
#     # exist_ok=True：目录已存在不报错
#     Path(FILE_PATH).mkdir(parents=True,exist_ok=True)
#
#     save_path = Path(FILE_PATH) / file.name   # 这是path方法的路径拼接
#
#     save_path.resolve()   # 获取这个地址的绝对路径
#
#     # 将上传的文件保存到本地../upload/files目录
#     file.save(save_path)
#
#     return respones.success(
#         msg="上传成功",
#         data={
#             "filename":file.name,
#             "path":save_path
#         }
#     )
#
#
# def service_spliter(file_id):
#     """
#     1、校验参数（file id）
#     2、使用langchain的文本读取器，读取文件内容
#     3、可以将文本转成markdown格式
#     4、使用langchain的文本切分器，根据二级标题和三级标题或者4级标题切分文本
#     :param file_id:
#     :return:
#     """
#     if not file_id:
#         return respones.missing_parameter(msg="文件id不允许为空")
#
#     # 获取存放路径文件夹中的文件名
#     files = Path(FILE_PATH)
#
#     file_name = []
#     for file in files.glob("*"):
#         file_name.append(str(file.resolve()))
#
#     if file_id not in file_name:
#         return respones.invalid_parameter(msg="文件不存在")
#
#
#
#
#
#
#
#
#
