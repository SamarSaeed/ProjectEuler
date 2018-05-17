import math

def is_prime(num):
    for x in range(2,int(math.sqrt(num)+1)):
        if num%x == 0:
            return False
    return True

prime_count = 0
number = 1
while prime_count < 10002:
    if is_prime(number):
        prime_count += 1
    number += 1

print number-1
