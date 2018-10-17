# 析构函数 __del__ 和垃圾回收机制

class Person:
    def __del__(self):
        print("销毁对象：{0}".format(self))

p1 = Person()
p2 = Person()

del p2
print("程序结束")