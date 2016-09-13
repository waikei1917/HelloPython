import datetime
import sys
import os

start = datetime.datetime.now()

i = 0
while i < 10000000:
    i = i+1
    
end = datetime.datetime.now()

print(end - start)

print(sys.path)
print(os.name)

