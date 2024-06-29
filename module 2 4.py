numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
primes_not =[]

for i in range(len(numbers)):
    is_prime=True
    if numbers[i] == 1:
        continue                    #не простое и не составное'
    elif numbers[i] == 2:
        is_prime = True
        primes.append(numbers[i])
    else:
        for j in range((numbers[i] - 2)):
            if numbers[i] % (j + 2) == 0:
                is_prime = False
                break
        if is_prime==True:
            primes.append(numbers[i])
        else:
            primes_not.append(numbers[i])

print('numbers =',numbers)
print('Primes:',primes)
print('Not Primes:',primes_not)


