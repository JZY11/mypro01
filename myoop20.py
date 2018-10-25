
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