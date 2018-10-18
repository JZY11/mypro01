# 测试 mro() 方法（查看类的目录结构）

class A:
    pass
class B(A):
    pass
class C(B):
    pass

print(C.mro())

# 重写 object的 __str__()
class Person:

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "名字是：{0}".format(self.name)

p = Person("小二")
# print(p)    # 不重写object的 __str__()时打印结果：<__main__.Person object at 0x002FAF30>

print(p)