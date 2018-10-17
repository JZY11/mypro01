# 测试类方法

class Student:
    company = "SXT"     # 类属性

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def printCompany(cls):  # 类方法
        print(cls.company)
#        print(self.name)     会报错，因为：在类方法和静态方法中不能调用实例属性(变量)和实例方法

Student.printCompany()


# 测试静态方法
class Student2:
    company1 = "BW"     # 类属性

    @staticmethod
    def add(a,b):       # 静态方法
        print("{0}+{1}={2}".format(a,b,(a+b)))
        return a+b

Student2.add(20,30)