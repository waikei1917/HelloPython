list = [1,2,3,4,5,6,7,8,9,10]

for int in list:
    print(int)
    if int == 7:
        break;

for int in list:
    if int == 7:
        break;
    else:
        print(int)
        
for int in list:
    if int == 7:
        continue;
    else:
        print(int)
else:
    print('defaults')