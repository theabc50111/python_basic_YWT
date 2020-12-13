# while stmt
m = int(input('Input factorial: '))
r = n = 1

while n <= m:
    r *= n # equal to r = r*n
    n += 1 # equal to n = n+1

print(f'{m}! = {r}')
