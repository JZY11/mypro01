# 局部变量和全局变量效率测试
import math
import time

def test01():
    start = time.time()
    for i in range(1000000):
        math.sqrt(30)
    end = time.time()

    print("耗时{0}".format((end - start)))

def test02():

    b = math.sqrt            # 这里的b就相当于是声明了一个局部变量
    start = time.time()
    for i in range(1000000):
        b(30)
    end = time.time()

    print("耗时{0}".format((end - start)))


test01()
test02()

'''
    局部变量的查询和访问速度比全局变量要快，优先考虑局部变量，尤其是在循环的时候。
    在特别强调效率的地方或则循环次数较多的地方，可以通过将全局变量转化为局部变量来提高运行速度。
'''








