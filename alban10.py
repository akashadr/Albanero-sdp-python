a=1/10
b=3602879701896397 / 2 ** 55
print(a,b)
if(a==b):
  print(True)
  
import math

print(format(math.pi, '.13g'))  # give 12 significant digits
#'3.14159265359'

print(format(math.pi, '.5f'))   # give 2 digits after the point
#'3.14'

print(math.pi)
#'3.141592653589793'

#How the format function works in Python:
x,y,z = 35.8679, 12.6354, 123.7803

print (('{0:.2f}, {2:.3f}, {1:.4f}').format(x,y,z))

#Output: 35.87, 123.782, 12.6354

p=1.12345
print('{:.3f}'.format(p))
print(f'{p:.3f}')

m=(round(.1, 10) + round(.1, 10) + round(.1, 10))
m1=round(.1,1)
n=round(.3, 10)
print(m)
print(n)
print(m1)



if(m==n): 
  print('True')
  
j = round(.1 + .1 + .1, 10)
k = round(.3, 10)
print(j)
print(k)

x = 9.5
print(x.as_integer_ratio())

m2=m1.hex()
print(m2)

m3=float.fromhex(m2)
print(m3)

print(sum([0.1] * 10) == 1.0)    #False
print(math.fsum([0.1] * 10) == 1.0) #True


q,r = divmod(31,7)

print(q,r)

