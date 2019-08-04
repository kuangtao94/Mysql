import pymysql

#查询
def select_MySQL():
    try:
        conn = pymysql.Connect(
            host="127.0.0.1",
            user="root",
            passwd="123456",
            db="one")
    except Exception as e:
        return e.args

    else:
        cur = conn.cursor()#创建游标，才能对mysql进行增删改查
        # sql = "select * from user where id = %s"
        # params = (1,) # 因为是元组
        #单个语句查询
        # cur.execute(sql,params)
        # data = cur.fetchone()
        # print(data)
        #多个语句查询
        cur.execute("select * from user")
        data = cur.fetchall()
        for item in data:
            print(item)
        #  列表推导式
        print([item  for item in data])
    finally:
        cur.close()
        conn.close()

#插入
def insert_MySQL():
    try:
        conn = pymysql.Connect(
            host="127.0.0.1",
            user="root",
            passwd="123456",
            db="one")
    except Exception as e:
        return e.args
    else:
        cur = conn.cursor()#创建游标，才能对mysql进行增删改查
        #单个语句插入
        # sql = "insert into user values(%s,%s,%s,%s)"
        # params = (4,"tao",23,"jiangxi") #元组
        #多个语句插入
        sql = 'insert into login values (%s,%s,%s)'
        params = [
            (1, 'weike','xian'),
            (2, 'weike','xian'),
            (3, 'weike','xian'),
            (4, 'weike','xian')
        ]

        cur.executemany(sql,params)
        conn.commit()
    finally:
        cur.close()
        conn.close()

#删除
def delete_MySQL():
    try:
        conn = pymysql.Connect(
            host="127.0.0.1",
            user="root",
            passwd="123456",
            db="one")
    except Exception as e:
        return e.args
    else:
        cur=conn.cursor()
        sql='delete from user where id=%s'
        params=(1,)
        cur.execute(sql,params)
        conn.commit()
    finally:
	    cur.close()
	    conn.close()

class MySql:
    def conn(self):
        con = pymysql.Connect(
            host="127.0.0.1",
            user="root",
            passwd="123456",
            db="one")
        return con

    #查询一条语句
    def get_one(self,sql,params):
        cur = self.conn().cursor() #创建游标
        cur.execute(sql,params)
        result = cur.fetchone()
        return result

def charls(username,password):
    opera = MySql()
    sql = "select * from login where username=%s and password=%s"
    params= (username,password)
    return opera.get_one(sql,params)

def info():
    username = input("请输入账号：\n")
    password = input("请输入密码：\n")
    result = charls(username,password)
    if result:
        print("正常登录,昵称:{0}".format(username))
    else:
        print("登录失败")

if __name__ == '__main__':
    info()




