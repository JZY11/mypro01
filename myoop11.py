# 继承       子类继承父类，则就继承了除了父类构造器外的其他所有成员

class Person:

    def __init__(self,name,age):        # 属性在构造器中定义
        self.name = name
        self.__age = age

    def say_age(self):
        print("你在说什么呢")


class Student(Person):      # 这就是子类继承父类的格式

    def __init__(self,name,age,score):
        Person.__init__(self,name,age)       # 子类必须要显示的调用父类的构造器，不然解释器不会调用
        self.score = score



stu = Student("小二",20,80)
stu.say_age()   # 子类继承了父类中的方法 say_age()

print(stu.name)
# print(stu.age)   子类虽然继承了父类中的私有方法&私有属性，但是不可以直接使用
print(dir(stu))     # dir(): 这个是个内置函数    可查看指定对象 stu 中的所有属性和方法
print(stu._Person__age)  # 这样用就可以

