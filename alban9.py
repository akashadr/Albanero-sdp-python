from datetime import time
Now = time()
print(Now)

import math
print(math.cos((math.pi*2)/3))

print(math.log(100, 10))


from datetime import date
now = date.today()
print(now)
#datetime.date(2003, 12, 2)

# dates support calendar arithmetic
birthday = date(2001, 7, 26)
age = now - birthday
print(age.days)
#14368


import zlib
s = b'witch which has which witches wrist watch'
print(len(s)) #41
t = zlib.compress(s)
print(len(t)) #37
h=zlib.decompress(t)
print(h)
#b'witch which has which witches wrist watch'

import doctest
print(doctest.testmod())