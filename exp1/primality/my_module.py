import math
def prime(n):
    if n < 1:
        return False
    if (n ==1)|(n==0):
        return False
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
            
    return True