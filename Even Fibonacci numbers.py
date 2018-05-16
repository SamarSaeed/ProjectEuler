sum=0
old = 1
new = 2
sumeven=2

print old
print new

while sum < 4000000:


    sum = old+new
    if sum % 2 == 0 :
        sumeven += sum

    old = new
    new = sum

   #print sum

print(sumeven)