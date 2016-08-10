list = [1,2,3,4,5,6,7,8,9,10,11,12]#定义list

print(list[5], '＃打印list的第6个元素')
print(list[-3], '＃打印倒数第三个元素')
print(len(list), '＃打印list长度')
print(list[2:10], '＃打印从第三到第11个元素')
print(list[2:10:2], '＃打印从第三到第11个元素，隔2打印一个')
print(list[2::2], '＃打印从第三到最尾，隔2打印一个')

list2 = [15,16];#定义list2

list.append(13)#list尾端添加一个元素
print('#list尾端添加一个元素:', 'list.append(13)')
list.extend(list2)#list尾端插进list2
print('#list尾端插进list2:', 'list.extend(list2)')

list.insert(5, 56);#list第6个元素处插入56
print("#list第6个元素处插入56: list.insert(5, 56)", '#输出：', list[5]);
list[4] = 33#修改list第5个元素为33
print('#修改list第5个元素为33: list[4] = 33', '#输出：', list[4]);

list[2] = list[2]*8;
print('#list第3个元素乘以8: list[2] = list[2]*8', '#输出：', list[2]);

del list[5:7];#list删除第6和第7个元素
print('#list删除第6和第7个元素:del list[5:7]', '#输出：',list);

list.remove(15)#查找list值为15的并移除
print('#list删除第6和第7个元素:del list[5:7]', '#输出：',list)

list.reverse()#把list倒过来
print('＃把list倒过来：list.reverse()','＃输出： ',list)

list3 = [2,3,4,1,5]#定义list3
list4 = sorted(list3)#定义list4等于排序好的list3
print('#定义list3','＃输出： ',list3)
print('#定义list4等于排序好的list3', '＃输出： ', list4)

list3.sort()#重新排序list3
print('#重新排序list3','＃输出： ', list3)



