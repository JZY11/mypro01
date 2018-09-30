'''
    选择结构的嵌套：
        选择结构是可以嵌套的，使用时一定要注意控制好不同级别代码块的缩进量，因为缩进量决定了代码的从属关系，语法格式如下：
        if 表达式1:
            语句块1
            if 表达式2:
                语句块2
            else：
                语句块3
        else：
            if 表达式4：
                语句块4
'''
# 练习一： 输入一个分数，分数在0 - 100之间，90以上是A，80以上是B，70以上是C，60以上是D，60以下是E
scope = int(input("请输入考试的具体分数："))
if scope > 100 or scope < 0:
    print("请输入一个0 - 100之间的一个具体分数值")
else:
    if scope > 90:
        print("A")
    elif scope >= 80:
        print("B")
    elif scope >= 70:
        print("C")
    elif scope >= 60:
        print("D")
    else:
        print("E")

# 练习二  是对练习一的一个优化(以后工作中若遇到很对的if else 的话可以这样考虑，这个算法还是挺不错的)
scope = int(input("请输入考试的具体分数："))
degree = "ABCDE"
num = 0
if scope > 100 or scope < 0:
    print("请输入一个0 - 100之间的一个具体分数值")
else:
    num = scope // 10  #   //表示的是去除余数而取整数部分
    if num < 6:
        num = 5

    print(degree[9 - num])











