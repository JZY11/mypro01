# 测试return返回语句

def my_avg(a,b):
    '''测试函数返回值'''

    print("计算两个数的平均值：{0},{1},{2}".format(a,b,(a+b)))
    return (a+b)/2

# 如下是函数的调用
c = my_avg(20,30)
print(c)

def test02():
    print("axt")
    print("gao")
    return       # return有两个作用：1、返回值   2、结束函数的执行

    print("hello")   # 上面的return已经将函数结束执行了    所以行代码执行不到了

test02()
            # 备注   如果没有return返回值的话     则默认返回的为 None

def test03(x,y,z):
    return [x*10,y*10,z*10]

d = test03(1,2,3)   # 直接就给返回一个列表，   也可以是元组或则字典
print(d)

def test04(j,k,l):
    return (j*10,k*10,l*10)
f = test04(5,4,3)
print(f)

def test05(b,m,w):
    return {b:b*10,m:m*10,w:w*10}
o = test05(7,8,9)
print(o)