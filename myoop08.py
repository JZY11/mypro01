# 测试私有属性、私有方法

class Employee:

    __company = "百战程序员"     # 类变量

    def __init__(self,name,age):
        self.name = name    # 现在name和age这两个属性都是公开的
        # self.age = age
        self.__age = age    # 这就是私有属性的定义方式

    def __work(self):       # 这是私有方法的定义(都是要有双下划线的)
        print("好好工作&学习")
        print("年龄：{0}".format(self.__age))  # 在类内部调用自己私有的属性
        print(Employee.__company)


e = Employee("小伟",18)      # 生成一个对象实例

print("---------------------")
print(e.name)
print("++++++++")
print(e._Employee__company)     # 外部调用时就用这样的格式
print(Employee._Employee__company)
print("_+_+_+_+_+_")
# print(e.age)  不能这样调用私有属性
# e.__work()    调用私有方法的方式不对

print(e._Employee__age)     # 对于私有属性要这样访问
e._Employee__work()