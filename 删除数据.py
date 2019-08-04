import pymysql

def Delete_From():
    #打开数据库链接
    db = pymysql.connect("localhost","root","123456","test")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL语句更新数据
    sql = """DELETE FROM student WHERE ID = %s"""%(3)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("删除数据成功")

    except Exception as e:
        print("删除数据失败：case%s"%e)
        #发生错误时回滚
        db.rollback()

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()

def main():
    Delete_From()

if __name__ == '__main__':
    main()