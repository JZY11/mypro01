class Student:  # 类名的首字母大写，多个单词用驼峰原则

    company = "aaa"
    count = 0

    def __init__(self,name,score):     # 构造函数  self 指当前对象本身(必须有，而且还要是第一个参数)
        self.name = name
        self.score = score
        Student.count = Student.count + 1

    def say_score(self):            # 普通函数
        print("{0}的分数是：{1}".format(self.name,self.score))

stu2 = Student  # Student 是一个类对象   把地址赋值给了变量 stu2

s1 = Student("小二", 18)
s1.say_score()

s2 = Student("隔壁的大神", 80)
s3 = Student("赵六子", 70)


print("一共创建了{0}个Student对象".format(Student.count))
