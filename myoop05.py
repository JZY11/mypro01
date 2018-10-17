# 测试可调用方法 __call__()

class SalaryAccount:
    '''工资计算类'''

    def __call__(self, salary):
        print("发工资啦")
        yearSalary = salary*12
        daySalary = salary//22.5
        hourSalary = daySalary//8

        return dict(yearSalary=yearSalary,monthSalary=salary,daySalary=daySalary,hourSalary=hourSalary)

s = SalaryAccount()
print(s(50000))     # 对象后面直接跟一个括号   这样它其实调用的就是 __call__() 这个方法