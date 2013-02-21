count = 3
primenum = [2]

#checking if the factor is a prime number
def checkprime(n):
    if not n and 1:
        return False
    for i in range (3, int(n**.5)+1,2):
        if n % i == 0:
            return False
    else:
        return True
        
#finding the factors in a number
#range just need to be until the squareroot of the number and we can skip all even numbers
while count <= 2000000:
    b = checkprime(count)
    if b == True:
        primenum.append(count)
    count += 2


print primenum[-1]
print sum(primenum)
