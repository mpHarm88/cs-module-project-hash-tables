# Your code here
import random
import math

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

# Create dictionary to hold repeated calculations   
factorial_hash = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here

    # If value has been calculated already then return the saved value
    if factorial_hash.get(f"{x}{y}") != None:
        print("Used hash dict")
        return factorial_hash.get(f"{x}{y}")
    
    # If value has not been calculated then calculate x, y
    else:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x+y)
        v %= 982451653
        factorial_hash[f"{x}{y}"] = v
        return v

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')