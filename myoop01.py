# 类的定义
class Student:  # 类名的首字母大写，多个单词用驼峰原则

    def __init__(self,name,score):     # 构造函数  self 指当前对象本身(必须有，而且还要是第一个参数)
        self.name = name
        self.score = score

    def say_score(self):            # 普通函数
        print("{0}的分数是：{1}".format(self.name,self.score))


s1 = Student("小二", 18)      # 类名后面跟括号就是调用构造函数(构造函数名字是固定的__init__)，生成一个对象，这里只有两个参数的原因是：解释器会默认的将这个对象的地址给到self
s1.say_score()

print(dir(s1))                 # 可以获得对象的所有属性跟方法（所有的）
print(s1.__dict__)             # 可直观的获得我们自己定义的属性（对象的属性字典）


class Men:
    pass            # pass 表示空语句（只是生命了这个类，但是里面啥都没有）

print(isinstance(s1,Student))