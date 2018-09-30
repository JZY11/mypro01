'''
测试zip() 并行迭代
'''

for i in [1,2,34,5]:  # 遍历一个列表
    print(i)

# 测试zip() 并行迭代：
names = ["小一","小二","小仨","小斯"]
ages = [14,15,34,65]
jobs = ["程序员","教师","医生","厨师"]

for name,age,job in zip(names,ages,jobs):  # 同上
    print("{0}--{1}--{2}".format(name,age,job))

print("++++++++++++++++++++++")

for i in range(4):
    print("{0}--{1}--{2}".format(names[i],ages[i],jobs[i]))



