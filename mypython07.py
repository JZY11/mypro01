'''
for循环和可迭代对象遍历：
    for循环通常用于可迭代对象的遍历，for循环的语法格式如下：
    for  变量  in  可迭代对象：
        循环体语句

    python包含以下几种可迭代对象：
        1、序列。 包含：字符串、列表、元组
        2、字典
        3、迭代器对象（iterator）
        4、生成器函数（generator）
'''

# 如：遍历一个元组
for x in (20, 30, 40):
    print(x)

# 遍历一个列表
for x in [20, 30, 40]:
    print(x*3)

# 遍历一个字符串
for y in "abcdefg":
    print(y)

# 遍历一个字典
d = {'name':'gaoqi','age':18,'address':'西二旗地铁站'}
for x in d: # 遍历字典中所有的key
    print(x)

for x in d.keys():  # 遍历字典中所有的key
    print(x)

for x in d.values():    # 遍历字典中所有的value
    print(x)

for x in d.items(): # 遍历字典中所有的“键值对”
    print(x)


'''
    range对象是一个迭代器对象 ，用来产生指定范围的数字序列，格式为：
        range(start,end [,step])
        生成的数值序列从start开始到end结束（不包含end），若没有填写start则默认从0开始，step是可选的步长，默认为1
        一下是简单示例：
            for i in range(10)      产生序列：0 1 2 3 4 5 6 7 8 9
            for i in range(3,10)    产生序列：3 4 5 6 7 8 9 
            for i in range(3,10,2)  产生序列：3 5 7 9
'''
for i in range(6):
    print(i)
print("==========================================")
sum_all = 0   #1 - 100 之间数字的累加和
sum_even = 0  #1 - 100之间偶数的累加和
sum_odd = 0   #1- 100之间奇数的累加和

for num in range(101):
    sum_all += num
    if num % 2 == 0: sum_even += num
    else:sum_odd += num

print("1 - 100 之间数字的累加和:",sum_all)
print("1 - 100之间偶数的累加和:",sum_even)
print("1- 100之间奇数的累加和:",sum_odd)











