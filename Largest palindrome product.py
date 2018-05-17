def is_palindrome(number):
    num = str(number)
    num_reverse = num[::-1]
    if num == num_reverse:
        return True
    else:
        return False
def largest_palindrome():
    max = 0
    for x in range(999, 99, -1):
        for y in range(999,99,-1):
         if is_palindrome(x*y):
           if x*y > max:
               max = x*y
    print max



largest_palindrome()