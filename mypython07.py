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

# range对象