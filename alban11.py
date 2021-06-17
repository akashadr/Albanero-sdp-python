import reprlib
print(reprlib.repr(set('super')))
#"{'a', 'c', 'd', 'e', 'f', 'g', ...}"

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta','yellow'], 'blue']]]
pprint.pprint(t, width=1)
"""[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]"""

import textwrap
doc = """The wrap() method is just like fill() except that it returns
    a list of strings instead of one big string with newlines to separate
    the wrapped lines."""

print(textwrap.fill(doc, width=40))

from string import Template
t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))

#'Nottinghamfolk send $10 to the ditch fund.'

from array import array
a = array('H', [4000, 10,700, 22222])
print(sum(a))
#26932
print(a[1:3])
#array('H', [10, 700])

from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())
#Handling task1

from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                     # rearrange the list into heap order
print(data)
heappush(data, -5)                 # add a new entry
l=[heappop(data) for i in range(3)]  # fetch the three smallest entries
print(l)
#[-5, 0, 1]


from decimal import *
print(round(Decimal('0.70') * Decimal('1.05'), 2))
print(Decimal('0.74'))
print(round(.70 * 1.05, 2))
#0.73
print('\n\n')

print(Decimal('1.00') % Decimal('.10'))
print(Decimal('0.000'))
#1.00 % 0.10
#0.09999999999999995

print(sum([Decimal('0.1')]*10) == Decimal('1.0'))
True
print(sum([0.1]*10) == 1.0)
False

print(Decimal(1) / Decimal(7))