class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
        
rev = Reverse('spam')
it=iter(rev)
#__main__.Reverse object at 0x00A1DB50>
for i in range(4):
  print(next(it))
  
print("\n\n")
  
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
   print(char)