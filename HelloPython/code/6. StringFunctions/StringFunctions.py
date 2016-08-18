string = 'string'

print(string[:4:2])

for letter in string:
    print(letter + '\n')
    
print(len(string))
print(string.count('t'))
print(string.title())
print(string.capitalize())

string = '-'
sequence = ['a','b','c','d','e','f','g','h']

print(string.join(sequence));

string = 'a-b--d-g-h-r-hg-d-d-g-f-e-t-y-q-f'
print(string.split('-'))

sequence = string.split('-')
for letter in sequence:
    print(letter);
    
