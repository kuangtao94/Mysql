import datetime
import pymysql

def insert_into():
    db = pymysql.connect("localhost","root","123456","test")
    cursor = db.cursor()

    #批量插入数据
    sql = """INSERT INTO  student VALUES(%s,%s,%s,%s,%s)"""
    params = [
        (1,"小王",23,"深圳",datetime.datetime.now()),
        (2,"小刘",24,"深圳",datetime.datetime.now()),
        (3,"小宋",25,"深圳",datetime.datetime.now())
    ]

    try:
        # 执行SQL语句
        cursor.executemany(sql,params)
        # 提交到数据库执行
        db.commit()
        print("插入数据成功")
    except Exception as e:
        print("插入数据失败：case%s"%e)
        # 如果发生错误则回滚
        db.rollback()
    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()

def main():
    insert_into()

if __name__ == '__main__':
    main()

