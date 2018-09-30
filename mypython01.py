print('hello pycharm!')
a = input("请输入一个小于10的数字：") # input()函数就可以将键盘输入的内容赋值给我们的变量，注意：input()函数默认返回的是一个字符串

if int(a) < 10:
    print(a)

'''
    在选择和循环结构中，条件表达式的值为False的情况如下：
        False、0、0.0、空值None、空序列对象(空列表[]、空元祖()、空集合{}、空字典{}、空字符串)、空range对象，空迭代对象
        
    其他情况，均为True
'''

#  if 3 < c and (c = 20)  错误的原因是：条件表达式中是不可以出现赋值操作符的 =

# 双分支选择结构：
num = input("请输入一个数字：")
if int(num) < 10:
    print(num)
else:
    print("不好意思，你输入的数字太大啦")


# 三元条件运算符，语法格式如下：
#                           条件为真时的值 if (条件表达式) else 条件为假时的值
num = input("请输入一个数字：")
print(num if int(num) < 10 else "数字太大啦")






