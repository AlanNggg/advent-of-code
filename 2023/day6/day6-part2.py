import time

# part 2
inputs = '''Time:        38     67     76     73
Distance:   234   1027   1157   1236'''.split('\n')

time = ''.join(inputs[0].split()[1:])
dist = ''.join(inputs[1].split()[1:])

ans = 1
#     x * (38 - x) = 234 = x^2 - 38x + 234
b = - int(time)
a = 1
c = int(dist)
print(f'x * ({time} - x) = {dist}')
x1 = int((-b - math.sqrt(b**2 - 4*a*c)) / (2 * a))
x2 = int((-b + math.sqrt(b**2 - 4*a*c)) / (2 * a))
    
ans = (x2-x1)
print(ans)