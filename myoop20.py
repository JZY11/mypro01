# 测试 has-a关系，使用组合   注意：is-a关系使用“继承”，从而实现子类拥有父类的属性和方法，它指代的是类似这样的关系：狗是动物  狗类就继承了动物类
# has-a关系，我们可以使用组合，也能实现一个类拥有另外一个类的属性和方法，has-a关系指代的是这样的关系：手机拥有CPU， MobilePhone has CPU

class MobilePhone:
    def __init__(self,cpu,screen):
        self.cpu = cpu
        self.screen = screen

class CPU:
    def calculate(self):
        print("计算计算...")
        print("cpu对象：",self)

class Screen:
    def show(self):
        print("来显示一个好看的画面")
        print("屏幕对象：",self)

m = MobilePhone(CPU(),Screen())
m.cpu.calculate()
m.screen.show()