import pymysql
"""
1、连接本地数据库
2、建立游标
3、创建表
4、插入表数据、查询表数据、更新表数据、删除表数据
"""

def create_table():
    #连接本地数据库
    db = pymysql.connect("localhost","root","123456","test")

    #创建游标
    cursor = db.cursor()
    #如果存在student表，则删除
    cursor.execute("DROP TABLE IF EXISTS student")

    #创建student表
    sql = """
        create table student(
        id int not null,
        name char(10),
        age int,
        address char(20),
        create_time datetime)
    """

    try:
        # 执行SQL语句
        cursor.execute(sql)
        print("创建数据库成功")
    except Exception as e:
        print("创建数据库失败：case%s"%e)
    finally:
        #关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()

def main():
    create_table()

if __name__ == "__main__":
    main()
