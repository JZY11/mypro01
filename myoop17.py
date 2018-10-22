# 测试一些特殊属性
class A:
   pass

class  B:
    pass

class C(B,A):
    def __init__(self,nn):
        self.nn = nn

    def cc(self):
        print("cc")


c = C(3)
# print(C.mro())      # 打印类的层次结构
# c.say()             # 解释器寻找方法是"从左向右"的方式寻找，此时会执行B类中的say

print(dir(c))
print(c.__dict__)               # 对象的属性字典
print(c.__class__)              # 对象所属的类
print(C.__bases__)              # 类的基类元组（多继承）
print(C.mro())                  # 类层次结构
print(A.__subclasses__())       # 子类列表