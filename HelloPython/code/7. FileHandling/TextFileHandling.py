txtfile = open('text.txt')
for line in txtfile:
    print(line, end='');
    
input = open('text.txt', 'r')
output = open('newtxt.txt','w')

for line in input:
    print(line, file=output, end='')
    
    