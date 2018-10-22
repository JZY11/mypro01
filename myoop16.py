# 特殊方法和运算符重载

a = 20
b = 30
c = a + b
d = a.__add__(b)

print("c =",c)
print("d =",d)

'''
    常见的特殊方法统计如下：
        方法          说明          例子
        
        __init__     构造方法      对象创建:p = Person()
        __del__      析构方法      对象回收
  __repr__,__str__   打印，转化     print(a)
        __call__     函数调用       a()
        __getattr__  点号运算       a.xxx    
'''

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):              # 重写了这个方法
        '''将对象转化为字符串一般用于print方法'''
        return "名字是:{0},年龄是:{1}".format(self.name,self.age)

    def __add__(self, other):       # 重写这个相加的方法
        if isinstance(other,Person):
            return self.name + other.name
        else:
            return "不是同类对象，不能相加"

    def __mul__(self, other):
        if isinstance(other,Person):
            return "{0}--{1}".format(self.name,other.name)
        else:
            return "不是同类对象，不能相乘"

p = Person("小二",18)
q = Person("大佬",20)
print(p)
x = p + q
print(x)