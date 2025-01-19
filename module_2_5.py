numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []        #список простых чисел
not_primes = []     #список составных чисел

for i in range(1, len(numbers)):    # так как 1 не простое и не составное число, его в расчет не берем
    is_prime = True
    for j in range(2, numbers [i]):
        if numbers[i] % j == 0:
            not_primes.append(numbers[i])
            is_prime = False
            break
    if is_prime:
        primes.append(numbers[i])

print('Простые числа:', primes)
print('Составные числа:', not_primes)