# _*_coding:utf-8_*_
#
# class pa(object):
#     def pri(self):
#         print(__name__)
#         print(__class__)
#         print(__class__.__name__)
#
# p = pa()
# p.pri()

def function():
    for i in range(10):
        yield i
# function()
# print(funciton().__next__())
# print(funciton().__next__())
# print(funciton().__next__())
# print(funciton().__next__())
# print(funciton().__next__())
# print(funciton().__next__())
print(next(function()))
print(next(function()))
print(next(function()))
print(next(function()))
