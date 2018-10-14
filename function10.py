# 浅拷贝与深拷贝
import copy
'''
    为了更加深入的理解参数传递的底层原理，有必要了解下浅拷贝与深拷贝，我们可以使用内置函数：copy(浅拷贝)、deepcopy(深拷贝)

    浅拷贝：不拷贝子对象的内容，只是拷贝了子对象的引用。
    深拷贝：会连子对象的内存也全部拷贝一份，对子对象的修改不会影响到原对象
'''

def testCopy():
    '''测试浅拷贝'''
    a = [10,20,[5,6]]
    b = copy.copy(a)

    print("a",a)
    print("b",b)

    b.append(30)
    b[2].append(7)
    print("浅拷贝后。。。")
    print("a", a)
    print("b", b)

testCopy()


