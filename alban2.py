l = [1,2,3,4,5]
l1 = [5,3,4,7,0]

l2=sorted(l1)
print(l1)
print(l2)

l1.sort()
print(l1)

#print(l.pop(len(l)-1))

#print(l)

#del l[2:3]
#print(l)

#l.clear()
#print(l)

#print(l.index(4,1,4))

#print(l.count(3))

a = [4,3,6,5,1,2,0]

#a.sort(reverse=True)

#a.reverse()

#b=a.copy()

#a.reverse()

#print(b)
#print(a)

#Using list as Queue

"""from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")        
queue.append("Graham")
print(queue)                 
print(queue.popleft())  
print(queue.popleft())   
print(queue)
"""   

"""squares = list(map(lambda x: x**2,range(10)))
print(squares)

s=[x**2 for x in range(10)]
print(s)"""

#print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

#vec = [[1,2,3], [4,5,6], [7,8,9]]
#print([num for elem in vec for num in elem])
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
          ]
  
#m=[[row[i] for row in matrix] for i in range(4)]
#print(m)


#a=[1,2,3]
#b=[4,5,6]

#print(tuple(zip(a,b)))

#del a[1:2]
#print(a)


"""t='h',

print(t)

t1=1,2,'a'

print(t1)

x,y,z=t1

print(x,y,z)"""

"""d={'a':1,'b':2,'c':3}

print(list(d))

print(dict((('sape', 4139), ('guido', 4127), ('jack', 4098))))

print(dict(sape=4139, guido=4127, jack=4098))

for i, v in enumerate(['tic', 'tac', 'toe']):
  print(v,i)
  
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
print(dict(zip(questions, answers)))

for i in reversed(range(1, 10, 2)):
  print(i)
"""

