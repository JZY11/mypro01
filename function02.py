# 测试形参和实参的基本用法

def printMax(a,b):

    '''这种格式就是对该函数的说明，这就是所谓的文档字符串也就是函数的注释'''


    # 注意  通过三个单引号可以定义多行字符串
    c = '''
        aaaaaaa
        bbbbbbbb
        ccccccccc
     '''
    print(c)

    if a>b:
        print(a,'最大值')
    else:
        print(b,'最大值')


printMax(20,15)
help(printMax.__doc__)  # 注意：这个函数使用来打印文档字符串的




