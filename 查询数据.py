import pymysql

def select_form():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "test")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = """SELECT * FROM student WHERE ID = %s"""%(2)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            name = row[1]
            age = row[2]
            address = row[3]
            create_time = row[4]
            print("id=%s,name=%s,age=%s,address=%s,create_time=%s"%\
                  (id,name,age,address,create_time))

    except Exception as e:
        print("查询出错：case%s"%e)

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()

def main():
    select_form()

if __name__ == '__main__':
    main()


