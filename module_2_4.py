numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [1,3,5,7,9]
not_primes = [17, 56, 1, 6, 2]

for i in numbers:
    is_prime = True
    if i == 1:
        continue
    else:
        for j in range (2, i-1) :
            if i % j == 0:
                is_prime = False
                break

    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

    print("Список:", numbers)
    print("Простые числа:", primes)
    print("Непростые числа:", not_primes)