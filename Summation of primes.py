import math

def is_prime(num):
    for x in range(2,int(math.sqrt(num)+1)):
        if num%x == 0:
            return False
    return True

counter = 1
sum = 0
while counter < 2000001:
    if is_prime(counter):
        sum+=counter
    counter += 1
print sum-1