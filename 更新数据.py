import pymysql

def Update_Set():
    #打开数据库链接
    db = pymysql.connect("localhost","root","123456","test")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    #SQL语句更新数据
    sql = """UPDATE student SET address = '东莞' WHERE ID = %s"""%(2)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("更新数据成功")

    except Exception as e:
        print("数据更新出错：case%s"%e)
        #发生错误是回滚
        db.rollback()

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()

def main():
    Update_Set()

if __name__ == '__main__':
    main()



