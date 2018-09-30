'''
while循环
    循环体里面的语句至少应该包含改变条件表达式的语句，以使循环趋于结束；否则就会变成一个死循环。
while循环的语法格式如下：
    while 条件表达式：
        循环体语句
'''
# 练习   利用while循环打印从0 - 10 的数字
num = 0
while num < 10:
    # print(num)
    print(num,end="\t")
    num += 1

print("==============================================================")

# 练习2  利用while循环，计算1 - 100 之间数字的累加和；计算1 - 100之间偶数的累加和；计算1- 100之间奇数的累加和
num = 0
sum_all = 0   #1 - 100 之间数字的累加和
sum_even = 0  #1 - 100之间偶数的累加和
sum_odd = 0   #1- 100之间奇数的累加和

while num<=100:
    sum_all += num
    if num % 2 == 0: sum_even += num
    else:sum_odd += num
    num += 1

print("1 - 100 之间数字的累加和:",sum_all)
print("1 - 100之间偶数的累加和:",sum_even)
print("1- 100之间奇数的累加和:",sum_odd)










