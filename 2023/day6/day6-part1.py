import math

# part 1
inputs = '''Time:        38     67     76     73
Distance:   234   1027   1157   1236'''.split('\n')

races = list(zip(inputs[0].split(), inputs[1].split()))

ans = 1
for time, dist in races[1:]:
    print(time, dist)
#     x * (38 - x) = 234 = x^2 - 38x + 234
    b = - int(time)
    a = 1
    c = int(dist)
    print(f'x * ({time} - x) = {dist}')
    x1 = int((-b - math.sqrt(b**2 - 4*a*c)) / (2 * a))
    x2 = int((-b + math.sqrt(b**2 - 4*a*c)) / (2 * a))
    
    ans *= (x2-x1)
print(ans)
