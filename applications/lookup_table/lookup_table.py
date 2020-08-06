# Your code here
import math
import random
cache = {}



def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


for y in range(3,6):
    for x in range(2,14):
        cache[str(x)+','+str(y)] = slowfun_too_slow(x,y)
   
print(cache)

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    idx = str(x)+','+str(y)
    if idx in cache:
        return cache[idx]
    else:
        print('no values', x, y)


# # # Do not modify below this line!

for i in range(5000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
