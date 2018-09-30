'''
    多分支选择结构：
        if 条件表达式1：
            语句1/语句块1
        elif 条件表达式2：
            语句2/语句块2
        .
        .
        .
        elif 条件表达式n：
            语句n/语句块n
        [else:                    方括号表示可选的意思
            语句n+1/语句块n+1
        ]
'''
# 练习：  输入一个学生色成绩，将其转化为简单描述：不及格(小于60)、及格(60-79)、良好(80-89)、优秀(90-100)
    # 方法一（使用完整的条件表达式）
# scope = int(input("请输入考试的具体分数"))
# grade = ''
# if(scope < 60):
#     grade = "不及格"
# if(60 <= scope < 80):
#     grade = "及格"
# if(80 <= scope < 90):
#     grade = "良好"
# if(90 <= scope <= 100):
#     grade = "优秀"
# print("分数是{0},等级是{1}".format(scope,grade))


# 方法二（利用多分支结构）   多分支结构，几个分支之间是有逻辑关系的，不能随意颠倒顺序
scope = int(input("请输入考试的具体分数："))
grade = ''
if scope < 60:
    grade = "不及格"
elif scope < 80:
    grade = "及格"
elif scope < 90:
    grade = "良好"
elif scope <= 100:
    grade = "优秀"
print("分数是{0},等级是{1}".format(scope,grade))  # {0}、{1} 是两个占位符，调用了字符串的format()方法来对字符串进行格式化






