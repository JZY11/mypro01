# 练习2   已知点的坐标(x,y),判断其所在的象限
x = int(input("请输入x轴的坐标："))
y = int(input("请输入y轴的坐标："))
if(x == 0 and y == 0):
    print("这是原点")
elif(x == 0):
    print("y轴")
elif (y == 0):
    print("x轴")
elif (x > 0 and y > 0):
    print("该坐标在第一象限")
elif (x > 0 and y < 0):
    print("该坐标在第二象限")
elif (x < 0 and y < 0):
    print("该坐标在第三象限")
else:
    print("该坐标在第四象限")
