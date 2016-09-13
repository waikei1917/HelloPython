txtfile = open('text.txt')
for line in txtfile:
    print(line, end='');
    
input = open('text.txt', 'r')
output = open('newtxt.txt','w')

for line in input:
    print(line, file=output, end='')
    
#write to anther file
buffersize = 10
infile = open('text.txt','r')
outfile = open('newBigFile.txt','w')

buffer = infile.read(buffersize)
bufferLimit = 500000

while bufferLimit >0:
    outfile.write(buffer)
    #print('.', end='')
    bufferLimit = bufferLimit - buffersize
    