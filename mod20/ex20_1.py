class Fibonacci():
    def __init__(self):
        self.a, self.b = (0, 1)
    def __iter__(self):
        return self
    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        if result <100:
            return result
        else:
            raise StopIteration

fibos = Fibonacci()
print(next(fibos)) #=> 0
print(next(fibos)) #=> 1
print(next(fibos)) #=> 1
print(next(fibos)) #=> 2
print("---------------------In for loop---------------------")
for i in fibos:
    print(i)