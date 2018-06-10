#!C:/python3 python3
import pymysql
import datetime

# 查询
def check(cur):
    for i in [1, 3, 7, 31]:
        add = datetime.timedelta(days=-i)
        dates = (datetime.datetime.now() + add).strftime("%Y-%m-%d")
        sql = 'select * from RB WHERE date = %s'
        cur.execute(sql, dates)
        for i in cur.fetchall():
            print(i[2])
# 增加
def add(cur,con,date):
    ask = input("are you sure to insert the data?")
    if ask =="1":
        with open(r"C:\Users\Administrator\Desktop\Dayly.txt","r",encoding="gbk") as f:
            data = ""
            while True:
                content = f.readline().strip()
                data += content
                data += " "
                # print(len(content))
                # print(data)
                if len(content) == 0:
                    break

        print(data)
        sql = 'insert into RB(date,content) VALUES (%s,%s)'
        cur.execute(sql, (date, data))
        con.commit()

    else:
        pass


def all(cur):
    sql = 'select * from RB'
    cur.execute(sql)
    for i in cur.fetchall():
        print(i)


def study():
    con = pymysql.connect(host = 'localhost', user = 'root',password = 'zhang',db= 'mystudy',charset='utf8')
    cur = con.cursor()
    date = str(datetime.datetime.now().strftime("%Y-%m-%d"))
    while True:
        flag = input('浇水-1，种树-2, 森林-3')
        if flag =='1':
            check(cur)
        elif flag =="2":
            add(cur,con,date)
        elif flag=="3":
            all(cur)
        else:
            cur.close()
            con.close()
            break

if __name__ == '__main__':
    study()
