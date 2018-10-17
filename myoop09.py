# 测试 @property (可将方法的调用转化为属性的调用) 最简化的使用

class Employee:

    @property
    def salary(self):
        print("salary run ...")
        return 10000

emp = Employee()
# emp.salary()   这是传统的调用方式

# emp.salary     # 这样就把方法的调用转化成了属性的调用（原因就是加了 @property ）
print(emp.salary)

# emp.salary = 20000    现在暂时不能去设置