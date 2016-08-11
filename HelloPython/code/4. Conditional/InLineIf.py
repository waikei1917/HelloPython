a,b = 1,0

if a==b:
    print(True)
else:
    print(False)
    
print(True if a==b else False)
print('This is True' if a==b else 'This is not True')

var = 'This is True' if a==b else 'This is not True'
print(var)