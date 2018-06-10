# print(type((i for i in range(6))))
# print(type([i for i in range(6)]))
# import re
# str = (str('a\nb\nc\n'))
# # str.replace(r"\\n", ' ')
# print(re.sub(r'\\n',' ',str))
# # print(str)

import gevent

def f(n,y):
    for i in range(n):
        print(gevent.getcurrent(), (i, y))

g1 = gevent.spawn(f, 5,6)
# g2 = gevent.spawn(f, 5)
# g3 = gevent.spawn(f, 5)
g1.join()
# g2.join()
# g3.join()