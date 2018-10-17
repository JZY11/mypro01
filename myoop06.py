# 继承与重写的案列

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_age(self):
        print(self.name,"的年龄是：",self.age)

    def say_name(self):
        print("我是：",self.name)


class Student(Person):
    def __init__(self,name,age,score):
        Person.__init__(self,name,age)      # 必须是显示的调用父类初始化方法，不然解释器不会去调用
        self.score = score

    def say_name(self):     # 子类重写了父类的方法，相当于把父类中的该方法给覆盖掉了，再去调用的时候自然调用的就是子类中的该方法
        '''重写了父类的该方法'''
        print("报告首长，我的名字是{0}".format(self.name))
s = Student("小二",20,80)
s.say_age()
s.say_name()