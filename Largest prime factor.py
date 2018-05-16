import math
def is_prime(num):
    for x in range(2,int(math.sqrt(num)+1)):
        if num%x == 0:
            return False
    return True

#The only even prime number is 2 and since number is even then 2 is not a divisor of number
dividor = 3
number = 600851475143
while dividor < number:
    if number%dividor == 0 and is_prime(dividor):
        print dividor
    dividor+=2

