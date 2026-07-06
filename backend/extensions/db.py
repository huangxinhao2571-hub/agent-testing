import psycopg2
from dbutils.pooled_db import PooledDB
from backend.config import DevConfig


Pool = PooledDB(
    # 使用 psycopg2 作为 PostgreSQL 的驱动
    creator=psycopg2,
    # 连接池允许的最大连接数
    maxconnections=10,
    # 初始化时，连接池中至少保留 2 个空闲连接
    mincached=2,
    # 连接池中最多缓存 5 个空闲连接
    maxcached=5,
    # 如果连接池暂时没有可用连接，是否等待
    blocking=True,
    # 建立连接后不额外执行初始化 SQL
    setsession=[],
    # ping=0 表示默认不主动检测连接是否可用
    ping=0,

    # 数据库地址和连接信息
    host=DevConfig.DB_HOST,
    port=DevConfig.DB_PORT,
    user=DevConfig.DB_USER,
    password=DevConfig.DB_PASSWORD,
    dbname=DevConfig.DB_NAME
)


def db_fetchone(sql,param:list):
    """
    查询 -- 一条结果
        查询一条结果的sql封装
        接口的业务逻辑service中，对数据库的操作封装
    :param sql: sql语句，%s
    :param param: 格式化输出 [xx]
    :return: 返回查询出来的一条数据（x，x，x），以元祖方式返回，没查到会返回None
    """
    conn = Pool.connection()
    cursor = conn.cursor()

    cursor.execute(sql,param)
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result


def db_fetchall(sql,param:list):
    """
    查询 -- 多条结果
        查询多条结果的返回
        接口的业务逻辑service中，对数据库的操作封装
    :param sql:
    :param param:
    :return: 以元祖的方式返回(x,x,x),(x,x,x)
    """
    conn = Pool.connection()

    cursor = conn.cursor()

    cursor.execute(sql,param)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result


def db_execute(sql, param: list):
    """
    增删改
        执行新增、删除、修改的sql封装
        接口的业务逻辑service中，对数据库的操作封装
    :param sql: sql语句，%s
    :param param: 格式化输出 [xx]
    :return: 返回受影响的行数
    """
    conn = Pool.connection()
    cursor = conn.cursor()

    try:
        cursor.execute(sql, param)
        conn.commit()
        result = cursor.rowcount
        return result
    finally:
        cursor.close()
        conn.close()


def db_execute_returning_one(sql, param: list):
    """
    增删改并返回一条结果。
        适合 INSERT ... RETURNING id 这类需要拿数据库生成值的 SQL。
    :param sql: 带 RETURNING 的 sql 语句
    :param param: 格式化参数 [xx]
    :return: 返回查询出来的一条数据，没返回则为 None
    """
    conn = Pool.connection()
    cursor = conn.cursor()

    try:
        cursor.execute(sql, param)
        result = cursor.fetchone()
        conn.commit()
        return result
    finally:
        cursor.close()
        conn.close()
