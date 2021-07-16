# 导包
import pymysql


# 创建工具类
class DBUnit:

    # 初始化变量
    __conn = None
    __cursor = None

    # 创建连接
    @classmethod
    def __get_conn(cls):
        if cls.__conn is None:
            cls.__conn = pymysql.connect(host="rm-bp14kd81y04x5ks05no.mysql.rds.aliyuncs.com",
                                         port=3306,
                                         user="test123",
                                         password="!Qwer1234",
                                         database="test123")
        return cls.__conn

    # 获取游标
    @classmethod
    def __get_cursor(cls):
        if cls.__cursor is None:
            cls.__cursor = cls.__get_conn().cursor()
        return cls.__cursor

    # 执行sql
    @classmethod
    def exe_sql(cls, sql):
        try:
            # 获取游标对象
            cursor = cls.__get_cursor()
            # 调用游标对象的execute方法，执行sql
            cursor.execute(sql)
            # 如果是查询
            if sql.split()[0].lower() == "select":
                # 返回所有数据
                return cursor.fetchall()
            # 否则
            else:
                # 提交事务
                cls.__conn.commit()
                # 返回受影响行
                return cursor.rowcount
        except Exception as e:
            # 事务回滚
            cls.__conn.rollback()
            # 打印异常信息
            print(e)
        finally:
            # 关闭游标
            cls.__close_cursor()
            # 关闭连接
            cls.__close_conn()

    # 关闭游标
    @classmethod
    def __close_cursor(cls):
        if cls.__cursor:
            cls.__cursor.close()
            cls.__cursor = None

    # 关闭连接
    @classmethod
    def __close_conn(cls):
        if cls.__conn:
            cls.__conn.close()
            cls.__conn = None


# 测试
# sql = "select * from login"
# data = DBUnit.exe_sql(sql)
# print(data)
