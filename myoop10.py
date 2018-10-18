# @property 装饰器的用法(getter setter)

class Employee:

    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter                      # 表示针对salary属性的一个设置
    def salary(self,salary):
        if 1000<salary<50000:
            self.__salary = salary
        else:
            print("信息录入错误！薪水在1000 - 50000之间，请您再次确认！")


'''
    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        if 1000<salary<50000:
            self.__salary = salary
        else:
            print("信息录入错误！薪水在1000 - 50000之间，请您再次确认！")

'''

emp1 = Employee("小二",30000)
# print(emp1.__salary)      这样访问是不行的   私有属性不能这样访问
#print(emp1.get_salary())

# emp1.salary = 20000
#emp1.set_salary(-20000)
#print(emp1.get_salary())


print(emp1.salary)
emp1.salary = 40000     # 这个赋值就是调用了 setter 方法
print(emp1.salary)


'''
    类的细节最好都封装起来（私有化）
'''