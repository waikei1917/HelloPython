a = 50 #正常定义，自动选类型
b = int(50.1) #float 强制转换 int
c = round(50.7) #输出int，取小数点后约数
d = float(50) #float 
e = "Hello Ass!" #字符串
f = '''
    HIHI
    Your
    ASS!!
    '''#输出段落
g = 'This is \na string'#断开字段
h = "Hello"
i = 'This is %s string' % h #连接字符串1
j = 'This is {} string'.format(h)#连接字符串2
k = (1,2,3,4,5,6,7,8,9)#tuple类型

l = [1,2,3,4,5,6,7,8]#list类型
l.append(9)#list 后方插入9

m = {'one':1, 'two':2, 'three':3}#dict类型1
n = {'id':5, 'name':'Tom'}#dict类型2

o = dict(
                  one = 1, two = 'two'
                  );#dict类型3

r = True #boolean类型

s, t = 0,1



print(a, " 正常定义，自动选类型")
print(b, " float 强制转换 int")
print(c, " 输出int，取小数点后约数")
print(d, " float")
print(e, " 字符串")
print(f, " 输出段落")
print(g, " 断开字段")
print(i, ' 连接字符串1')
print(j, ' 连接字符串2')
print(k, ' 类型：', type(k))
print(l, ' 类型：', type(l))
print(l, ' list后方插入9')
print(l[2], ' 打印出第2个元素')
print(l[2:6], ' 打印出第二到第六个元素')
print(l[:6], ' 打印全部第6个之前的元素')
print(m, '类型：', type(m))
print(n, '类型：', type(n))
print(o, '类型： ', type(o))
print(r, '类型： ', type(r))

if s==t:
    print(True)
else:
    print(False)
    
print("")



