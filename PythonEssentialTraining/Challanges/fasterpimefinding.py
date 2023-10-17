def allPrimeUpTo(num):
    newPrime = [2]
    if num > 2:
        for n in range(2,num+1):
            if n == 2:
                newPrime.append(2)

            for prime in newPrime:
                if n % prime == 0:
                    break
            else:
                newPrime.append(n)
        
    return newPrime

print(allPrimeUpTo(23))