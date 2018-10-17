# 测试方法的动态性

class Person:

    def work(self):
        print("我在上班！")

def play_game(s):
    print("{0}在玩游戏".format(s))

def work2(s):               # 该方法与Person类一毛钱关系都没有
    print("上班就要好好工作")

p = Person()
Person.play = play_game
p.work()
p.play()

Person.work = work2     # 这就修改了所定义的方法
p.work()

'''
    谨记：
        方法和函数都是对象，即一切都是对象
'''
