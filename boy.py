import pymysql
import datetime


class Sboy(object):

    def __init__(self):
        self.con = pymysql.connect(host='localhost', user='root', password='zhang', db='mystudy', charset='utf8')
        self.cur = self.con.cursor()
        self.date = str(datetime.datetime.now().strftime("%Y-%m-%d"))
        self.Datas = list()


    def check(self):
        for i in [1, 3, 7, 15]:
            add = datetime.timedelta(days=-i)
            dates = (datetime.datetime.now() + add).strftime("%Y-%m-%d")
            sql = 'select * from RB WHERE date = %s'
            self.cur.execute(sql, dates)
            for element in self.cur.fetchall():
                self.Datas.append(element)
        return self.Datas


    # 增加
    def add(self):
        ask = input("are you sure to insert the data?")
        if ask == "yes":
            with open(r"C:\Users\Administrator\Desktop\Dayly.txt", "r", encoding="gbk") as f:
                self.data = ""
                while True:
                    content = f.readline().strip()
                    self.data += content
                    self.data += " "
                    # print(len(content))
                    # print(data)
                    if len(content) == 0:
                        break
            sql = 'insert into RB(date,content) VALUES (%s,%s)'
            self.cur.execute(sql, (self.date, self.data))
            self.con.commit()

        else:
            pass


    def all(self):
        sql = 'select * from RB'
        self.cur.execute(sql)
        for i in self.cur.fetchall():
            print(i)

    def start(self):
        while True:
            flag = input('浇水-1，种树-2, 森林-3')
            if flag == '1':
                self.check()
            elif flag == "2":
                self.add()
            elif flag == "3":
                self.all()
            else:
                self.cur.close()
                self.con.close()
                break


if __name__ =="__main__":
	boy =Sboy()
	boy.start()