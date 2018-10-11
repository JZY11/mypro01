import turtle

'''
    练习：绘制不同颜色的多个同心圆
'''

t = turtle.Pen()

my_colors = ('red','green','yellow','black','blue')  # 自定义一个元组，里面存的是想要的颜色
t.width(4)
t.speed(0) # 0 是最快的

for i in range(6):      # 0 1 2 3 4 5
    t.penup()

    t.goto(0,-i*50)     # 0 -50 -100 -150 -200
    t.pendown()
    t.color(my_colors[i%len(my_colors)])
    t.circle(50 + i*50)       # 50 100 150 200 250


'''
    t.goto(0,-100) # 将画笔提起向下移动100
    t.circle(200)
    
    t.goto(0,-200) # 将画笔提起向下移动100
    t.circle(300)
'''
turtle.done() # 程序执行完窗口仍在



