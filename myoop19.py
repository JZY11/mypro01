# 测试组合   如果不用组合的话那就用继承，子类继承父类，同时就拥有了父类中的方法
# 实现继承来实现代码的复用，同样的使用组合也是可以达到同样目的的

class A1:
    def say_a1(self):
        print("a1,a1,a1")

class B1(A1):
    pass

b1 = B1()
b1.say_a1()


# 下面是使用组合
class A2:
    def say_a2(self):
        print("a2,a2,a2")

class B2:
    def __init__(self,a):
        self.a = a

b2 = B2(A2())
b2.a.say_a2()
