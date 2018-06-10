import datetime


class Calenderboy(object):
    def __init__(self):
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")

    def write(self, dic):
        # data = input("learing content:")
        lis = list()
        with open(r"C:\Users\Administrator\Desktop\Dayly.txt","r",encoding="gbk") as f:
            while True:
                data = f.readline().strip()
                if len(data):
                    lis.append(data)
                    # print(lis)
                else:
                    dic[self.date] =lis
                    break
            print(dic)


    def back(self, dic):
        for i in [1, 3, 7, 15]:
            add = datetime.timedelta(days=-i)
            dates = (datetime.datetime.now() +add).strftime("%Y-%m-%d")
            try:
                data = dic[dates]
                print(dates,data)
            # except Exception as f:
            #     print(f)
            except:
                pass
                print(dates)



if __name__ == '__main__':
    f = open("Daily.db", "r")
    # print(f.read(),end="\n")
    # f.seek(0)
    dic = eval(f.read())
    f.close()
    zhang = Calenderboy()
    while True:
        signal = input("write-1/back-2")
        if signal == "1":
            zhang.write(dic)
        elif signal == "2":
            try:
                zhang.back(dic)
            except Exception as error:
                print(error)
        else:
            f = open("Daily.db", "w")
            f.write(str(dic))
            f.close()
            break

