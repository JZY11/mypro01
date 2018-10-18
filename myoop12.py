# 测试方法的重写

class Person:

    def __init__(self,name,age):        # 属性在构造器中定义
        self.name = name
        self.__age = age

    def say_age(self):
        print("我的年龄：",self.__age)

    def say_name(self):
        print("我的名字是{0}".format(self.name))


class Student(Person):      # 这就是子类继承父类的格式

    def __init__(self,name,age,score):
        Person.__init__(self,name,age)       # 子类必须要显示的调用父类的构造器，不然解释器不会调用
        self.score = score

    def say_name(self):
        '''重写了父类中的该方法（相当于把父类中的该方法给覆盖掉了）'''
        print("报告首长，我的名字是{0}".format(self.name))

s = Student("小二",18,87)
s.say_age()
s.say_name()