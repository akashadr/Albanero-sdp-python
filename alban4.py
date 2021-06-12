i = 'f'

S = str(i)
R = repr(i)

print(S,R)

if(str(i)==repr(i)):
  print('yes')
  
Hello =  repr('hello, world\n')

print(Hello)

import math
print(f'The value of pi is approximately {math.pi:.3f}.')
#The value of pi is approximately 3.142.

table = {'Sjoen': 4162, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
  print(f'{name:8} ==> {phone:6d}')


animals = '9'
print(f'My hovercraft is full of {animals!r}.')

print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

