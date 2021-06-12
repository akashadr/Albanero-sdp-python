def foo(name, **kwds):
  return 'name' in kwds

print(*{'a': 2,'b' : 3})
print(*((1,2),2,3))

l = [1,2,3,4]

print(*l)

def parrot(voltage, state='a stiff', action='voom'):
  print("-- This parrot wouldn't", action, end=' ')
  print("if you put", voltage, "volts through it.", end=' ')
  print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
#This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

args = [3, 6]
l=list(range(*args))
print(l)
#[3, 4, 5]

def make_incrementor(n):
  return lambda x: x + n

f = make_incrementor(42)
print(f(0))
#42
print(f(1))
#43

def ano(l,n):
  #l1=list(map(lambda x:x+n,l))
  l1=[x+n for x in l]
  print(l1)

l=[1,2,3]
ano(l,4)

def my_function():
  """Do nothing, but document it.

No, really, it doesn't do anything.
   """
  pass

print(my_function.__doc__)
