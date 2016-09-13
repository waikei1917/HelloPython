#write a new file call rabbit.jpg
buffersize = 100000
input = open('labbit.jpg','rb')
output = open('rabbit.jpg', 'wb')
buffer = input.read(buffersize)

while len(buffer):
    output.write(buffer)
    print('.', end='')
    buffer = input.read(buffersize)
    
